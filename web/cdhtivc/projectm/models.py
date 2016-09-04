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
    userName=models.CharField('用户名',max_length=20)
    userGroup=models.CharField('职位',max_length=20)
    passWord=models.CharField('密码',max_length=20,default='12345678x')
    department=models.CharField('部门',max_length=10,choices=departChoices,default='ts')

    
    def __unicode__(self):
        #print type(self.userName)
        return self.userName
    

class IndustryType(models.Model):#行业类型
    industryName=models.CharField(max_length=20)
    industryDescibe=models.CharField(max_length=20)


'''
class FinancialSituation(models.Model):#财务状况
    indexChoices=[('income','销售收入'),('netProfit','净利润')]
    yearChoices=[('2015','2015年'),('2016','2016年')]
    #companyName=models.ForeignKey('CompanyData')
    financialIndex=models.CharField(max_length=10,choices=indexChoices,default='income')
    yearIndex=models.CharField(max_length=4,choices=yearChoices,default='2015')
    financialData=models.FloatField(default=None)
'''


class CompanyData(models.Model):
    industryChioce=[('xxjs','新一代信息技术'),('swzy','生物制药'),('jnhb','节能环保'),('zbzz','高端装备制造')]#行业类型
    natureChioce=[('yx','有限公司'),('gf','股份有限公司'),('td','团队')]
    suggestChioce=[('ybgz','一般关注'),('zdgz','重点关注'),('zh','暂缓项目'),('lx','立项'),('gh','已过会'),('ybk','已拨款')]
    companyId=models.CharField("项目编号",max_length=8,default=None)#项目编号
    companyCreateDate=models.DateField("入库日期",default=None)#入库日期
    companyProjectSetUpTime=models.DateField("立项日期",default=None)#立项日期
    companyProjectPassDate=models.DateField("过会日期",default=None)#过会日期
    companyUpdateDate=models.DateTimeField("更新时间",default=None)#更新日期
    companyName=models.CharField("公司名称",max_length=200)#公司名称
    companyNature=models.CharField("公司类型",max_length=10,choices=natureChioce,default='yx')#公司性质
    companyAddress=models.CharField("公司地址",max_length=500,default=None)#地址
    companyRegisteredDate=models.DateField('注册时间',default=None)#公司成立日期
    #industry=models.CharField(max_length=20)#行业
    registeredCaptital=models.CharField("注册资本",max_length=100,default=None)#注册资本
    contactPeople=models.CharField("联系人",max_length=10,default=None)#联系人
    contactPhone=models.CharField("联系电话",max_length=50,default=None)#联系方式
    companyAbstract=models.TextField("公司基本情况",default=None)#公司基本情况
    companyRemarks=models.TextField("公司其他备注情况",default=None)#公司其他备注情况
    companyFinancialSituation=models.TextField("公司财务指标",default=None)#公司财务指标
    companyFinancialNeeds=models.TextField("公司融资需求",default=None)#公司融资需求
    companyFollowSuggest=models.CharField("跟进建议",max_length=10,choices=suggestChioce,default='ybgz')#跟进建议
    user=models.ForeignKey(User,default=None,verbose_name='入库人')#入库人
    industry=models.CharField("行业类型",max_length=10,choices=industryChioce,default='xxjs')#行业类型
    #financialSituation=models.ForeignKey(FinancialSituation,default=None)

    def __unicode__(self):
        return self.companyName



    