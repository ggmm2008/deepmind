# -*- coding:utf-8 -*-  
#===============================
#  
#+==============================

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from .models import CompanyData,User
from .forms import CompanyDataForm,LoginForm
from django.db.models import Count
import json
from django.http import JsonResponse

# Create your views here.


'''
class IndexView(generic.ListView):
    template_name='projectm/index.html'
    context_object_name='CompanyDataList'

    
    def get_queryset(self):
        return CompanyData.objects.order_by('id')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['userId'] = request.session['userId']
        return context    
'''

class DetailView(generic.DeleteView):
    model=CompanyData
    template_name='projectm/detail.html'


def index(request):
    context={'userId':request.session['userId']}
    #获取本周入库详细信息

    #获取累计本月累计入库

    #获取累计本季度入库

    #获取累计本年入库
    return render(request, 'projectm/index.html',{'context':context})
    



def check(request):
    '''
    print 'kkk'
    user = request.GET['a']
    passwd = request.GET['b']
    print user,passwd
    #用户验证
    try:
        userInfo=User.objects.get(userName=user)
        print userInfo.userName,userInfo.passWord
        if userInfo.passWord==passwd:
            return HttpResponseRedirect('/projectm/')
    except User.DoesNotExist:
        errroInfo='你输入的信息有误！'
        return HttpResponseRedirect('/projectm/login/')
    '''



def login(request):
    print request.user
    errorStr=''         
    if request.method=='POST':           
        #print  form.cleaned_data
        form = LoginForm(request.POST)
        if form.is_valid():            
            user=form.cleaned_data['user']
            passwd=form.cleaned_data['password']
            #用户验证
            try:
                userInfo=User.objects.get(userName=user)
                print userInfo.userName,userInfo.passWord
                if userInfo.passWord==passwd:
                    #存入session
                    request.session['userId']=userInfo.id
                    return HttpResponseRedirect('/projectm/')#登录成功，跳转
            except User.DoesNotExist:
                errorStr='user/password error!'  
        else:
            errorStr='input error!'                  
    else:
        form=LoginForm()
    return render(request, 'projectm/login.html',{'form':form,'errorStr':errorStr})


def error(request):
     return render(request, 'projectm/error.html')


