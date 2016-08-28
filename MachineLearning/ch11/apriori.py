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
    #set_trace()
    C1=[]
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return map(frozenset,C1)


def scanD(D,CK,minSupport):
    #set_trace()
    ssCnt={}
    for tid in D:
        for can in CK:  
            if can.issubset(tid):
                if not ssCnt.has_key(can):ssCnt[can]=1
                else:ssCnt[can]+=1
    numItems=float(len(D))
    retList=[]
    supportData={}
    for key in ssCnt:
        support=ssCnt[key]/numItems
        if support>=minSupport:
            retList.insert(0,key)
        supportData[key]=support
    #set_trace()
    return retList,supportData


def apriorGen(LK,k):#creates CK
    retList=[]
    lenLK=len(LK)
    #set_trace()
    for i in range(lenLK):
        for j in range(i+1,lenLK):
            L1=list(LK[i])[:k-2];L2=list(LK[j])[:k-2]
            L1.sort();L2.sort()
            if L1==L2:
                retList.append(LK[i]|LK[j])
    return retList


def apriori(dataSet,minSupport=0.5):
    C1=createC1(dataSet)
    D=map(set,dataSet)
    L1,supportData=scanD(D,C1,minSupport)
    L=[L1]
    k=2
    while (len(L[k-2])>0):
        CK=apriorGen(L[k-2],k)
        LK,supK=scanD(D,CK,minSupport)
        supportData.update(supK)
        L.append(LK)
        k+=1
    return L,supportData


def generateRules(L,supportData,minConf=0.7):
    set_trace()
    bigRuleList=[]
    for i in range(1,len(L)):
        for freqSet in L[i]:
            H1=[frozenset([item]) for item in freqSet]
            if(i>1):
                rulesFromConseq(freqSet,H1,supportData,bigRuleList,minConf)
            else:
                calcConf(freqSet,H1,supportData,bigRuleList,minConf)
        return bigRuleList


def calcConf(freqSet,H,supportData,brl,minConf=0.7):
    set_trace()
    prunedH=[]
    for conseq in H:
        conf=supportData[freqSet]/supportData[freqSet-conseq]
        if conf>=minConfL
            print freqSet-conf,'-->',conseq,'conf:',conf
            brl.append((freqSet-conseq,conseq,conf))
            prunedH.append(conseq)
    return prunedH


def rulesFromConseq(freqSet,H,supportData,brl,minConf=0.7):
    set_trace()
    m=len(H[0])
    if (len(freqSet)>(m+1)):
        Hmp1=apriorGen(H,m+1)
        Hmp1=calcConf(freqSet,Hmp1,supportData,brl,minConf)
        if (len(Hmp1)>1):
            rulesFromConseq(freqSet,Hmp1,supportData,brl,minConf)