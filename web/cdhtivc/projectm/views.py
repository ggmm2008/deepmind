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
def index(request):
    CompanyDataList=CompanyData.objects.order_by('id')
    #output=','.join([p.companyName for p in CompanyDataList])
    context={'CompanyDataList':CompanyDataList}
    return render(request,'projectm/index.html',context)

def detail(request,id):
    try:
        companys=CompanyData.objects.get(pk=id)
    except CompanyData.DoesNotExist:
        raise Http404('该公司未入库')
    return render(request,'projectm/detail.html',{'companys':companys})
'''


class IndexView(generic.ListView):
    template_name='projectm/index.html'
    context_object_name='CompanyDataList'
    tt='kkkk'
    
    def get_queryset(self):
        return CompanyData.objects.order_by('id')

class DetailView(generic.DeleteView):
    model=CompanyData
    template_name='projectm/detail.html'


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CompanyDataForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CompanyDataForm()

    return render(request, 'projectm/name.html', {'form': form})


def test(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CompanyDataForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CompanyDataForm()

    return render(request, 'projectm/test.html', {'form': form})




 
def ajax_list(request):
    a = range(100)
    return JsonResponse(a, safe=False)
 
def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)

def add(request):
    a = request.GET['a']
    print a
    #b = request.GET['b']
    #a = int(a)
   # b = int(b)
    s=list(CompanyData.objects.filter(companyName__contains=a))
    print type(s)
    print s
    if len(s)>0:
        str1=s
    else:
        str1="项目未入库！"
    

    return HttpResponse(str1)

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
        print "post"       
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
                    request.session[userId]=userInfo.id
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