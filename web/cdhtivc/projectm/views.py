# -*- coding:utf-8 -*-  
#===============================
#  
#+==============================

#from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from .models import CompanyData


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
    
    def get_queryset(self):
        return CompanyData.objects.order_by('id')

class DetailView(generic.DeleteView):
    model=CompanyData
    template_name='projectm/detail.html'