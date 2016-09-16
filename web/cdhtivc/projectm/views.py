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

import datetime

# Create your views here.




def detail(request,companyId=0000):
    context={'companyId':companyId}
    if check(request):#session检查
        try:
            if companyId!=0000:
                company=CompanyData.objects.get(id=companyId)#已有数据
                form=CompanyDataForm(instance=company)
            else:
                print '000000000000000'
                company=CompanyData(user=request.session.get('userName',default=None))#新建记录
                form=CompanyDataForm(instance=company)
        except CompanyData.DoesNotExist:
            return  HttpResponse("未查到数据！")            
    else:
        return HttpResponseRedirect('/projectm/login/')#验证失败
    return render(request, 'projectm/detail.html',{'form':form,'context':context})    


def index(request):
    context={}
    if check(request):#session检查        
        context['totalFileds']=tFileds()
        context['userId']=request.session.get('userId',default=None)
        context['userName']=request.session.get('userName',default=None)
        #累计信息
        countAll=CompanyData.objects.count
        userCount=CompanyData.objects.filter(user=context['userId']).count()
        context['countAll']=countAll
        context['userCount']=userCount
        d = datetime.datetime.now()
        dateResult=month_get(d)        
        if request.method=='POST':#如果是查询            
            searchStr=request.POST['searchStr']
            #print 'searchStr:',searchStr
            companys=CompanyData.objects.filter(companyName__contains=searchStr)
            companysCount=CompanyData.objects.filter(companyName__contains=searchStr).count()            
            context['companysCount']=companysCount
            context['companys']=companys
            #searchStr=''
        else:#第一次进入            
            #获取本周入库
            #获取上周时间            
            companys=CompanyData.objects.filter(companyCreateDate__range=(dateResult['date_from'],dateResult['date_end']))#<=2016-09-05
            companysCount=CompanyData.objects.filter(companyCreateDate__range=(dateResult['date_from'],dateResult['date_end'])).count()
            context['companysCount']=companysCount
            #获取累计本季度入库
            context['companys']=companys
            #获取累计本年入库
       
    else:
        return HttpResponseRedirect('/projectm/login/')#验证失败
    return render(request, 'projectm/index.html',{'context':context})
    
def tFileds():#汇总信息字段
    totalFileds={'merger':uncode2Str(CompanyData.objects.values_list('industry').distinct())}
    totalFileds['companyFollowSuggest']=uncode2Str(CompanyData.objects.values_list('companyFollowSuggest').distinct())
    totalFileds['user']=uncode2Str(CompanyData.objects.values_list('user').distinct())
    #print totalFileds
    return totalFileds


def uncode2Str(str):#字符转换
    result=[]
    for i in  range(len(str)):
        #print str[i][0]
        result.append(str[i][0].encode('utf-8'))
    return result



def week_get(d):#获取上周日期区间    
    dayscount = datetime.timedelta(days=d.isoweekday())
    dayto = d - dayscount
    sixdays = datetime.timedelta(days=6)
    dayfrom = dayto - sixdays
    date_from = datetime.datetime(dayfrom.year, dayfrom.month, dayfrom.day, 0, 0, 0)
    date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
    #print '---'.join([str(date_from), str(date_to)])
    result={'date_from':date_from,'date_end':date_to}
    return result

def month_get(d):#获取上月日期区间
    dayscount = datetime.timedelta(days=d.day)
    dayto = d - dayscount
    date_from = datetime.datetime(dayto.year, dayto.month, 1, 0, 0, 0)
    date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
    #print '---'.join([str(date_from), str(date_to)])
    result={'date_from':date_from,'date_end':date_to}
    return result

def check(request):#session检查
    userId=request.session.get('userId',default=None)
    print userId
    checkValue=bool
    if userId!=None:
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
                    request.session['userName']=userInfo.userName
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
    return  HttpResponse("You're logged out.close this windows")


    
def updateView(request,companyId=0):    
    if check(request):#session检查
        context={'companyId':companyId}
        resStr='error'
        if request.method=='POST' and int(companyId)!=0: #更新数据     
            tempObject=CompanyData.objects.get(pk=companyId)
            form = CompanyDataForm(request.POST,instance=tempObject)
            form.save()
            resStr='update seucess'
        
        else:#创建新记录
            print "new"
            form = CompanyDataForm(request.POST)
            if form.is_valid():
                instances=form.save()
                resStr='create new data'           
            else:
                return render(request, 'projectm/detail.html',{'form':form,'context':context})
        return  HttpResponse("You're "+resStr)
    else:
        return HttpResponseRedirect('/projectm/login/')#验证失败
    return render(request, 'projectm/index.html',{'context':context})



