# -*- coding:utf-8 -*-  
#===============================
#  
#+==============================

from django.conf.urls import url
from .import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^(?P<companyId>[0-9]+)/$',views.detail,name='detail')

]