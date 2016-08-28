# -*- coding:utf-8 -*-  
#===============================
#  
#+==============================

from django.contrib import admin
from .models import CompanyData,User,IndustryType,FinancialSituation
# Register your models here.

class CompanyDataAdmin(admin.ModelAdmin):
    fieldsets=[('基本情况',{'fields':['companyName','companyNature','companyAddress','companyRegisteredDate',\
                ]}),]

class UserAdmin(admin.ModelAdmin):
    list_display=('userName','userGroup','department')


admin.site.register(CompanyData)
admin.site.register(User,UserAdmin)
admin.site.register(IndustryType)
admin.site.register(FinancialSituation)
