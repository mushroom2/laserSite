
from django.conf.urls import include, url
from django.contrib import admin
from registration.forms import RegistrationForm
from registration.views import RegistrationView
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


register = RegistrationView.as_view()

urlpatterns = [
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.urls')),
    url(r'^accounts/register/$', register, {
        'form_class': RegistrationForm,
        'backend': 'registration.backends.default.DefaultBackend',

    }),
    url('', include('registration.urls')),
    url(r'^', include('blog.urls')),
    url(r'^photologue/', include('photologue.urls', namespace="photologue")),
    url(r'^$', TemplateView.as_view(template_name="homepage.html"), name='homepage'),
    url(r'^shop/', include('magaz.urls')),
    url(r'^cart/', include('cart1.urls', namespace='cart1')),
    url(r'^redactor/', include('redactor.urls', namespace='redactor' )),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

