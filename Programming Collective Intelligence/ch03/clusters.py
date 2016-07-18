
# -*- coding:utf-8 -*-  

import pandas as pd
import numpy as np
from ipdb import set_trace
from math import sqrt
from pearson import *

class bicluster:
    #set_trace()
    def __init__(self,vec,left=None,right=None,distance=0.0,id=None):
        self.left=left
        self.right=right
        self.vec=vec
        self.id=id
        self.distance=distance

    def printData():
        print ("left:%s,right:%s,id:%s,distance:%f") % (self.lef,self.right,self.id,self.distance)


def loadSet():
    dataArr=pd.read_csv('blogdata.csv',index_col=1,encoding='utf-8')
    return dataArr


def pearson(v1,v2):
    #set_trace()
    x=np.array(v1)
    y=np.array(v2)

    t1=sum((x-x.mean())*(y-y.mean()))
    t2=pow(sum(pow(x-x.mean(),2)),0.5)*pow(sum(pow(y-y.mean(),2)),0.5)
    t=t1/t2  
    #set_trace()
    #print "t1:%f,t2:%f,t:%f" % (t1,t2,t)

    return t


def hcluster(data,distance=pearson):
    set_trace()###############################
    distances={}
    currentclustid=-1
    #开始聚类
    clust=[bicluster(np.array(data.ix[i]),id=i) for i in range(len(data))]
    #set_trace()###############################
    while len(clust)>1:
        lowestpair=(0,1)
        closest=distance(clust[0].vec,clust[1].vec)
        for i in range(len(clust)):
            for j in range(i+1,len(clust)):
                if(clust[i].id,clust[i].id) not in distances:
                    distances[(clust[i].id,clust[j].id)]=distance(clust[i].vec,clust[j].vec)
                d=distances[(clust[i].id,clust[j].id)]
                if d<closest:
                    closest=d
                    lowestpair=(i,j)
        #set_trace()################
        mergevec=[(clust[lowestpair[0]].vec[i]+clust[lowestpair[1]].vec[i])/2.0 for i in  range(len(clust[0].vec))]
        newcluster=bicluster(mergevec,left=clust[lowestpair[0]],right=clust[lowestpair[1]],distance=closest,id=currentclustid)
        #set_trace()################
        currentclustid-=1
        del clust[lowestpair[1]]
        del clust[lowestpair[0]]
        clust.append(newcluster)
    
    return clust[0]


def printclust(clust,labels=None,n=0):
    for i in range(n):print ' ',
    if clust.id<0:
        print '-'
    else:
        if labels==None:print clust.id
        else:print labels[clust.id]
    
    if clust.left!=None:printclust(clust.left,labels=labels,n=n+1)
    if clust.right!=None:printclust(clust.right,labels=labels,n=n+1)
    





