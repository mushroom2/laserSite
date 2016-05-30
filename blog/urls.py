from django.conf.urls import url, include, patterns

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^xxx/$', views.xxx, name='xxx'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', views.show_article, name='article'),
    url(r'^partner/(?P<partner_id>[0-9]+)/$', views.about, name='partners')

]