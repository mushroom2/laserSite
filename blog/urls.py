from django.conf.urls import url, include, patterns

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^news/$', views.xxx, name='xxx'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', views.show_article, name='article'),
    url(r'^partner/(?P<partner_id>[0-9]+)/$', views.about, name='partners'),
    url(r'^thanks/$', views.thenks, name='thenks'),
    url(r'^simpleform/$', views.mysimpleform, name='form'),
    url(r'^userlogin/$', views.userauth, name = 'userlogin'),
    url(r'^userlogout/$', views.logout_view, name= 'logout'),
    url(r'^complete/$', views.thenksshop, name='complete')
]