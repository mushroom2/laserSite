from django.conf.urls import url, include, patterns

from . import views

urlpatterns=[
    url(r'^$', views.shop, name='shop'),
    url(r'product/(?P<good_id>[0-9]+)/$', views.show_goods, name='prises'),
    url(r'(?P<slag_url>[\-\d\w]+)/$', views.cat_detail, name='category')
]
#