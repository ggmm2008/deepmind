# -*- coding:utf-8 -*-  
#===============================
#   EMAIL 垃圾邮件过滤测试
#   我靠  
#+==============================

import re
from ipdb import set_trace
from bayes import *
import numpy as np 


def loadDataSet(fileName):

    f=open(fileName,'r')
    myStr=''.join(f.readlines())
    regEx=re.compile('\\W*')
    #set_trace()
    myStr=regEx.split(myStr)
    Str1=[tok.lower() for tok in  myStr if len(tok)>2]
    return Str1


def spamTest():
    docList=[];classList=[];fullText=[]
    for i in range(1,26):
        worldList=loadDataSet('email/spam/%d.txt' % i)
        docList.append(worldList)
        #print worldList
        fullText.extend(worldList)
        classList.append(1)
        worldList=loadDataSet('email/ham/%d.txt' % i)
        docList.append(worldList)
        fullText.extend(worldList)
        classList.append(0)
    vocabList=createVocabList(docList)
    trainingSet=range(50);testSet=[]
    for i in range(10):
        randIndex=int(np.random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat=[];trainClasses=[]
    print testSet
    print trainingSet
    #set_trace()
    for docIndex in trainingSet:
        #set_trace()
        #print docIndex        
        trainMat.append(setOfWords2Vec(vocabList,docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam=trainNB0(trainMat,trainClasses)
    errorCount=0
    for docIndex in testSet:
        wordVector=setOfWords2Vec(vocabList,docList[docIndex])
        #set_trace()
        if classifyNb(wordVector,p0V,p1V,pSpam)!=classList[docIndex]:
            errorCount+=1
    print 'the error rate is:' ,float(errorCount)/len(testSet)

