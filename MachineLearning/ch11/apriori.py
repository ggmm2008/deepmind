# -*- coding:utf-8 -*-  
#机器学习，微信号13547948911

from numpy import *
from ipdb import set_trace
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd


def loadDataSet():
    return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]


def createC1(dataSet):
    set_trace()
    C1=[]
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return map(frozenset,C1)


def scanD(D,CK,minSupport):
    set_trace()
    ssCnt={}
    for tid in D:
        for can in CK:  
            if can.issubset(tid):
                if not sscnt.has_key(can):ssCnt[can]=1
                else:ssCnt[can]+=1
    numItems=float(len(D))
    retList=[]
    supportData={}
    for key in ssCnt:
        support=ssCnt[key]/numItems
        if support>=minSupport:
            retList.insert(0,key)
        supportData[key]=support
    return retList,supportData


