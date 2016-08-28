from django.conf.urls import url, include, patterns

from . import views

urlpatterns = [
    url(r'^cabinet/$', views.cabinet, name='cabinet'),
    url(r'^siteform/$', views.siteform, name='siteform'),
    url(r'^skypeform/$', views.skypeform, name='skypeform'),
    url(r'^professionform/$', views.professionform, name='professionform'),
    url(r'^numbform/$', views.numbform, name='numbform'),
    url(r'^aboutform/$', views.aboutform, name='aboutform'),
    url(r'^avatarform/$', views.avatarform, name='avatarform'),
    url(r'^$', views.shop, name='shop'),
    url(r'product/(?P<good_id>[0-9]+)/$', views.show_goods, name='prises'),
    url(r'(?P<slag_url>[\-\d\w]+)/$', views.cat_detail, name='category'),
]
