# -*- coding:utf-8 -*-  
#===============================
#  
#+==============================


from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    #userId=models.AutoField()
    departChoices=[('ts','天使投资部'),('ct','创业投资部')]
    userName=models.CharField(max_length=20)
    userGroup=models.CharField(max_length=20)
    department=models.CharField(max_length=10,choices=departChoices,default='ts')

    
    def __unicode__(self):
        #print type(self.userName)
        return self.userName
    

class IndustryType(models.Model):#行业类型
    industryName=models.CharField(max_length=20)
    industryDescibe=models.CharField(max_length=20)



class FinancialSituation(models.Model):#财务状况
    indexChoices=[('income','销售收入'),('netProfit','净利润')]
    yearChoices=[('2015','2015年'),('2016','2016年')]
    companyName=models.ForeignKey('CompanyData')
    financialIndex=models.CharField(max_length=10,choices=indexChoices,default='income')
    yearIndex=models.CharField(max_length=4,choices=yearChoices,default='2015')
    financialData=models.FloatField(default=None)



class CompanyData(models.Model):
    industryChioce=[('xxjs','信息技术'),('swzy','生物制药')]
    natureChioce=[('yx','有限公司'),('gf','股份有限公司')]
    companyId=models.AutoField(primary_key=True,default=1)#编号
    companyCreateDate=models.DateField(default=None)#入库日期
    companyUpdateDate=models.DateTimeField(default=None)#更新日期
    companyName=models.CharField(max_length=200)#公司名称
    companyNature=models.CharField(max_length=10,choices=industryChioce,default='yx')#公司性质
    companyAddress=models.CharField(max_length=500)#地址
    companyRegisteredDate=models.DateField('registered date')#公司成立日期
    #industry=models.CharField(max_length=20)#行业
    registeredCaptital=models.FloatField()#注册资本
    legalRepresentative=models.CharField(max_length=10)#法定代表
    legalPhone=models.CharField(max_length=50)#法人联系方式
    companyAbstract=models.TextField()#公司基本情况
    user=models.ForeignKey(User,default=None)
    industry=models.CharField(max_length=10,choices=industryChioce,default='xxjs')
    financialSituation=models.ForeignKey(FinancialSituation,default=None)

    def __unicode__(self):
        return self.companyName



    