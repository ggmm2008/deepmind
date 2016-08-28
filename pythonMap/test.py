# -*- coding:utf-8 -*-  

import requests 
import numpy as  np 
import pandas as pd
from ipdb import set_trace

def loadData():
    dataMat=pd.read_csv('data.csv')
    return dataMat

def requestData(dataMat):    
    #set_trace()
    for i in range(2501,len(dataMat)):
    #循环查询地址 每天<2000次调用
        key={'address':dataMat.ix[i,0],'city':'重庆'}
        txt='http://restapi.amap.com/v3/geocode/geo?key=5a65393af609a75927a1809fd3be56a1'
        r = requests.get(txt,params=key)
        print 'search data:%d' % i
        print '\n'
        if (len(r.json()['geocodes']))>0:
            t=(r.json()['geocodes'][0]['location']).encode('utf-8').split(',')
            #print "search data:",t+'\n'
            dataMat.ix[i,2]=t[0]
            dataMat.ix[i,3]=t[1]
    return dataMat



