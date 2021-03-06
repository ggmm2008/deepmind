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
from django.db.models import Count,Max
from django.views.generic.edit import UpdateView

import datetime
import calendar

# Create your views here.




def detail(request,companyId=0000):
    context={'companyId':companyId}
    context['userName']=request.session.get('userName',default=None)
    if check(request):#session检查
        try:
            if companyId!=0000:
                company=CompanyData.objects.get(id=companyId)#已有数据
                company.companyUpdateDate=datetime.datetime.now()
                form=CompanyDataForm(instance=company)                
            else:
                print " create new company"
                company=CompanyData(user=request.session.get('userName',default=None))#新建记录
                company.companyUpdateDate=datetime.datetime.now().strftime('%Y-%m-%d')
                company.companyCreateDate=datetime.datetime.now().strftime('%Y-%m-%d')
                company.companyId=int(CompanyData.objects.latest('companyId').companyId)+1
                form=CompanyDataForm(instance=company)
                
        except CompanyData.DoesNotExist:
            return  HttpResponse("未查到数据！")            
    else:
        return HttpResponseRedirect('/projectm/login/')#验证失败
    return render(request, 'projectm/detail.html',{'form':form,'context':context})    


def index(request,key='',value=''):
    print key,value
    context={} 
    totalFiledsName={'':'none','company':'公司名称','industry':'行业分类','follow':'跟进建议','dateLti':'入库时间','user':'投资经理'}
    context['seachKeyValue']={'key':totalFiledsName[key],'value':value}
    if check(request):#session检查        
        d = datetime.datetime.now()
        context['totalFileds']=tFileds(d)#统计字段
        context['tCount']=tCount(context['totalFileds'])#统计信息汇总
        context['userId']=request.session.get('userId',default=None)
        context['userName']=request.session.get('userName',default=None)
        #累计信息
        countAll=CompanyData.objects.count
        userCount=CompanyData.objects.filter(user=context['userId']).count()
        context['countAll']=countAll
        context['userCount']=userCount   
 
        if request.method=='POST':#入库查询            
            searchStr=request.POST['searchStr']
            context['seachKeyValue']={'key':totalFiledsName['company'],'value':searchStr}
            #print 'searchStr:',searchStr
            companys=CompanyData.objects.filter(companyName__contains=searchStr).order_by('-id')
            companysCount=CompanyData.objects.filter(companyName__contains=searchStr).count()            
            context['companysCount']=companysCount
            context['companys']=companys
            #searchStr=''
        else:          
            
            #时间查询            
            if key=='dateLti' or key=='':
                dateResult=thisWeek_get(d)               
                if value.encode('utf-8')=='上周':
                    dateResult=week_get(d)                     
                if value.encode('utf-8')=='上月':
                    dateResult=month_get(d)  
                if value.encode('utf-8')=='本周':
                    dateResult=thisWeek_get(d)
                if value.encode('utf-8')=='本月':
                    dateResult=thisMonth_get(d)    
                #print dateResult
                companys=CompanyData.objects.filter(companyCreateDate__range=(dateResult['date_from'],dateResult['date_end'])).order_by('-id')
                companysCount=CompanyData.objects.filter(companyCreateDate__range=(dateResult['date_from'],dateResult['date_end'])).count()
                context['companysCount']=companysCount                
                context['companys']=companys
            #行业查询 
            if key=='industry':
                companys=CompanyData.objects.filter(industry__contains=value.encode('utf-8')).order_by('-id')
                companysCount=CompanyData.objects.filter(industry__contains=value.encode('utf-8')).count()            
                context['companysCount']=companysCount
                context['companys']=companys
            
            #跟进状态查询 
            if key=='follow':
                companys=CompanyData.objects.filter(companyFollowSuggest__contains=value.encode('utf-8')).order_by('-id')
                companysCount=CompanyData.objects.filter(companyFollowSuggest__contains=value.encode('utf-8')).count()            
                context['companysCount']=companysCount
                context['companys']=companys
            
            #投资经理查询 
            if key=='user':
                companys=CompanyData.objects.filter(user__contains=value.encode('utf-8')).order_by('-id')
                companysCount=CompanyData.objects.filter(user__contains=value.encode('utf-8')).count()            
                context['companysCount']=companysCount
                context['companys']=companys

       
    else:
        return HttpResponseRedirect('/projectm/login/')#验证失败
    return render(request, 'projectm/index.html',{'context':context})
    
def tFileds(d):#汇总信息字段
    totalFileds={'industry':uncode2Str(CompanyData.objects.values_list('industry').distinct())}
    totalFileds['companyFollowSuggest']=uncode2Str(CompanyData.objects.values_list('companyFollowSuggest').distinct())
    totalFileds['user']=uncode2Str(CompanyData.objects.values_list('user').distinct())
    #获取日期区间
    bz=thisWeek_get(d)['date_from'].strftime('%m/%d')+'--'+thisWeek_get(d)['date_end'].strftime('%m/%d')
    sz=week_get(d)['date_from'].strftime('%m/%d')+'--'+week_get(d)['date_end'].strftime('%m/%d')
    by=thisMonth_get(d)['date_from'].strftime('%m/%d')+'--'+thisMonth_get(d)['date_end'].strftime('%m/%d')
    sy=month_get(d)['date_from'].strftime('%m/%d')+'--'+month_get(d)['date_end'].strftime('%m/%d')      
    totalFileds['dateLit']={u'本周':bz,u'上周':sz,u'本月':by,u'上月':sy}



    #print totalFileds
    return totalFileds

def tCount(totalFileds): #汇总信息计算      
    tCountResult={}    
    #print totalFileds
    for tmp in totalFileds.keys():
        tCountResult[tmp]=[]
        #print 'tmp:',tmp
        if tmp=='industry':
        #industry 汇总
            for i in range(len(totalFileds[tmp])):                
                tCountResult[tmp].append({'key':totalFileds[tmp][i],'value':CompanyData.objects.filter(industry__contains=totalFileds[tmp][i]).count()})               
        
        if tmp=='companyFollowSuggest':
        #companyFollowSuggest 汇总
            for i in range(len(totalFileds[tmp])):
                tCountResult[tmp].append({'key':totalFileds[tmp][i],'value':CompanyData.objects.filter(companyFollowSuggest__contains=totalFileds[tmp][i]).count()})
           
        if tmp=='user':
        #user 汇总
            for i in range(len(totalFileds[tmp])):
                tCountResult[tmp].append({'key':totalFileds[tmp][i],'value':CompanyData.objects.filter(user__contains=totalFileds[tmp][i]).count()})   
    #print 'tCountResult',tCountResult
    return tCountResult


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

def thisWeek_get(d):#本周
    midWeek=d.weekday()
    date_from=d-datetime.timedelta(days=(midWeek-(midWeek-1)))
    date_to=d+datetime.timedelta(days=(6-midWeek))
    result={'date_from':date_from,'date_end':date_to}
    #print '---'.join([str(date_from), str(date_to)])
    return result

def thisMonth_get(d):#本月
    yearT=d.year
    monthT=d.month
    monthRange = calendar.monthrange(yearT,monthT)
    date_from = datetime.datetime(yearT, monthT, 1, 0, 0, 0)
    date_to = date_from+datetime.timedelta(days=(monthRange[1]-1))
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
    form = LoginForm(request.POST)
    return render(request, 'projectm/login.html',{'form':form})


    
def updateView(request,companyId=0):    
    if check(request):#session检查
        context={'companyId':companyId}
        stateStr='error'
        if request.method=='POST' and int(companyId)!=0: #更新数据     
            tempObject=CompanyData.objects.get(pk=companyId)
            #tempObject.companyUpdateDate=datetime.datetime.now()
            form = CompanyDataForm(request.POST,instance=tempObject)          
            context['userName']=request.session.get('userName',default=None)
            if tempObject.user==context['userName']:
                if form.is_valid():
                    form.save()
                    context['stateStr']='数据更新成功'
                else:
                    print form.errors
                    context['stateStr']='数据输入有误，请重新输入！' 
            else:#非创建人 无权修改数据
                context['stateStr']='非创建人，无权修改数据！'
        
        else:#创建新记录
            print "new"
            form = CompanyDataForm(request.POST)
            if form.is_valid():
                instances=form.save()
                context['stateStr']='创建新公司成功！'  
        return  render(request, 'projectm/detail.html',{'form':form,'context':context})
    else:
        return HttpResponseRedirect('/projectm/login/')#验证失败
    return render(request, 'projectm/index.html',{'context':context})



