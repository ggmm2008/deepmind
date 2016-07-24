# -*- coding:utf-8 -*-  

from numpy import *
from ipdb import set_trace
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

def loadDataSet(fileName):
    set_trace()
    dataMat=[]
    fr=open(fileName)
    for line in fr.readlines():
        curLine=line.strip().split('\t')
        fltLine=map(float,curLine)
        dataMat.append(fltLine)
    return mat(dataMat)
    

def distEclud(vecA,vecB):
    return sqrt(sum(power(vecA-vecB,2)))


def randCent(dataSet,k):
    n=shape(dataSet)[1]
    centroids=mat(zeros((k,n)))
    for j in range(n):
        minJ=min(dataSet[:,j])
        rangeJ=float(max(dataSet[:,j])-minJ)
        centroids[:,j]=minJ+rangeJ*random.rand(k,1)
    return centroids

#显示图标
def plotData(centroids,dataMat,clusterAssment):
    colors=['b','g','c','m','y','k']
    dataMatPD=pd.concat([pd.DataFrame(dataMat,columns=['key1','key2'])\
        ,pd.DataFrame(clusterAssment,columns=['key3','key4'])],axis=1)
    fig=plt.figure(str(datetime.now())[-6:])
    plt.scatter(centroids[:,0],centroids[:,1],color='r',figure=fig)    
    for name,group in dataMatPD.groupby('key3'):
        plt.scatter(group.ix[:,0],group.ix[:,1],label=name,\
            figure=fig,color=colors[(random.randint(0,len(colors)))])    


def kMeans(dataSet,k,distMeas=distEclud,createCent=randCent):
    #set_trace()
    m=shape(dataSet)[0]
    clusterAssment=mat(zeros((m,2)))
    centroids=createCent(dataSet,k)
    clusterchanged=True
    while clusterchanged:
        clusterchanged=False
        for i in range(m):
            #set_trace()
            minDist=inf;minIndex=-1
            for j in range(k):
                distJI=distMeas(centroids[j,:],dataSet[i,:])
                print i,j
                if distJI<minDist:
                    minDist=distJI;minIndex=j
            if clusterAssment[i,0]!=minIndex:clusterchanged=True
            clusterAssment[i,:]=minIndex,minDist**2
        print centroids
        for cent in range(k):
            #set_trace()
            ptsInClust=dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]
            centroids[cent,:]=mean(ptsInClust,axis=0)
        #set_trace()
        plotData(centroids,dataSet,clusterAssment)
    return centroids,clusterAssment
    


def biKmeans(dataSet,k,distMeas=distEclud):
    #set_trace()
    m=shape(dataSet)[0]
    clusterAssment=mat(zeros((m,2)))
    centroid0=mean(dataSet,axis=0).tolist()[0]
    centList=[centroid0]
    for j in range(m):
        clusterAssment[j,1]=distMeas(mat(centroid0),dataSet[j,:])**2
    set_trace()
    while(len(centList)<k):
        lowestSSE=inf
        for i in range(len(centList)):
            print "i:%d" % i
            ptsInCurrCluster=dataSet[nonzero(clusterAssment[:,0].A==i)[0],:]
            centroidMat,splitClustAss=kMeans(ptsInCurrCluster,2,distMeas)
            sseSplit=sum(splitClustAss[:,1])
            sseNotSplit=sum(clusterAssment[nonzero(clusterAssment[:,0].A!=i)[0],1])
            print "sseSplit,and notSplit:",sseSplit,sseNotSplit
            if(sseSplit+sseNotSplit)<lowestSSE:
                bestCentToSplit=i
                bestNewCents=centroidMat
                bestClustAss=splitClustAss.copy()
                lowestSSE=sseSplit+sseNotSplit
        bestClustAss[nonzero(bestClustAss[:,0].A==1)[0],0]=len(centList)
        bestClustAss[nonzero(bestClustAss[:,0].A==0)[0],0]=bestCentToSplit
        print 'the bestCentToSplit is:',bestCentToSplit
        print 'the len of bestClustAss is:',len(bestClustAss)
        centList[bestCentToSplit]=bestNewCents[0,:]
        centList.append(bestNewCents[1,:])
        clusterAssment[nonzero(clusterAssment[:,0].A==bestCentToSplit)[0],:]=bestClustAss
    
    return mat(centList),clusterAssment



