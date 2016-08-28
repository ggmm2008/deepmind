# -*- coding:utf-8 -*-  
#===============================
#  
#+==============================

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("hello projects")

def detail(request,companyId):
    return HttpResponse("公司序号:%s"  % companyId.encode('utf-8'))