# -*- coding:utf-8 -*-  
#===============================
#  
#+==============================

from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^(?P<companyId>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<pk>[0-9]+)/update/$',views.UpdateView.as_view(),name='companydataupdate'),
    url(r'^error/$', views.error, name='error'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^check/$', views.check, name='check'),
    
    
]