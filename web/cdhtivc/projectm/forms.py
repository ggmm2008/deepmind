# -*- coding:utf-8 -*-  
#===============================
#  
#+==============================

from django.forms import ModelForm,Form
from django import forms
from projectm.models import CompanyData

class CompanyDataForm(ModelForm):
    class Meta:
        model=CompanyData
        fields = '__all__'

class LoginForm(forms.Form):
    user=forms.CharField(label='userName',max_length=20,strip=True)
    password=forms.CharField(label='password',max_length=20,strip=True,widget=forms.PasswordInput)