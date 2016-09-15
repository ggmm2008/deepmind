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
from django.db.models import Count
from django.views.generic.edit import UpdateView


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


class CompanyDetailView(generic.DetailView):
    model=CompanyData
    template_name='projectm/detail.html'
    
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        print 'kkkk'
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['companyInfo'] = CompanyData.objects.filter(companyData__id=self.object.name)
        print self.object.name
        return context

    def get_object(self,queryset=None):
        # Call the superclass
        obj = super(CompanyDetailView, self).get_object()
        print obj
        # Record the last accessed date
        #object.last_accessed = timezone.now()
        
        # Return the object
        return obj
'''







def detail(request,companyId):
    context={'companyId':companyId}
    if check(request):#session检查
        try:
            company=CompanyData.objects.get(id=companyId)
            form=CompanyDataForm(instance=company)
            if request.method=='POST':
                 pass
        except CompanyData.DoesNotExist:
            return  HttpResponse("未查到数据！")
    else:
        return HttpResponseRedirect('/projectm/login/')#验证失败
    return render(request, 'projectm/detail.html',{'form':form,'context':context})    


def index(request):
    context={}
    if check(request):#session检查
        context={'userId':request.session.get('userId',default=None)}
        #累计信息
        countAll=CompanyData.objects.count
        userCount=CompanyData.objects.filter(user_id=context['userId']).count()
        context['countAll']=countAll
        context['userCount']=userCount
        #获取本周入库
        listByWeek=CompanyData.objects.filter(companyCreateDate__lte='2016-09-05')#<=2016-09-05
        #获取累计本季度入库
        context['listByWeek']=listByWeek
        #获取累计本年入库
    else:
        return HttpResponseRedirect('/projectm/login/')#验证失败
    return render(request, 'projectm/index.html',{'context':context})
    



def check(request):#session检查
    userId=request.session.get('userId',default=None)
    print userId
    checkValue=bool
    if userId<>None:
        print 'userId:',userId
        checkValue=True

    else:
        checkValue=False
    
    return checkValue


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


def logout(request):
    try:
        del request.session['userId']
    except KeyError:
        pass
    return  HttpResponse("You're logged out.")

class CompanyDataUpdate(UpdateView):
    form_class=CompanyDataForm
    model=CompanyData
    fields='__all__'
    template_name_suffix='detail.html'

    
    def get_queryset(self):
        print 'lkkk'
        queryset = super(CompanyDataUpdate, self).get_queryset()
            
        return queryset
    


def error(request):
     return render(request, 'projectm/error.html')


