# -*- coding:utf-8 -*-  
#===============================
#  
#+==============================

from django.forms import ModelForm
from projectm.models import CompanyData

class CompanyDataForm(ModelForm):
    class Meta:
        model=CompanyData
        fields = '__all__'