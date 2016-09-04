# -*- coding:utf-8 -*-  
#===============================
#  
#+==============================

from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    url(r'^name/$',views.get_name,name='get_name'),
    url(r'test/$',views.test,name='test'),
    url(r'^ajax_list/$', views.ajax_list, name='ajax-list'),
    url(r'^ajax_dict/$', views.ajax_dict, name='ajax-dict'),
    url(r'^error/$', views.error, name='error'),
    url(r'^login/$', views.login, name='login'),
    url(r'^check/$', views.check, name='check'),
    
    
]