# -*- coding:utf-8 -*-  
#===============================
#  
#+==============================

from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(u'^total/(?P<key>\w*)/(?P<value>[\u4e00-\u9fa5]+)/$',views.index,name='totalindex'),
    url(r'^new/$', views.detail,name='detail'),
    url(r'^(?P<companyId>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<companyId>[0-9]+)/update/$',views.updateView,name='updateView'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^check/$', views.check, name='check'),
   
    
    
]