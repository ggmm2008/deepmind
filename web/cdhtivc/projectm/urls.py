# -*- coding:utf-8 -*-  
#===============================
#  
#+==============================

from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    url(r'^error/$', views.error, name='error'),
    url(r'^login/$', views.login, name='login'),
    url(r'^check/$', views.check, name='check'),
    
    
]