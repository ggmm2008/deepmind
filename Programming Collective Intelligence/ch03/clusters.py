import pandas as pd
import numpy as np
from ipdb import set_trace
from math import sqrt
from pearson import *

class bicluster:
    def __init__(self,vec,left=None,right=None,distance=0.0):
        self.left=left
        self.right=right
        self.vec=vec
        self.id=id
        self.distance=distance


def loadSet():
    dataArr=pd.read_table('blogdata.txt',sep='\t',index_col=0)
    return dataArr


def hcluster(rows,distance=pearson):
    distances={}
    currentclustid=-1

    #开始聚类
    clust=[bicluster(rows[i],id=i) for i in range(len(rows))]

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
    
    mergevec=[(clust[lowestpair[0]].vec[i]+clust[lowestpair[1]].vec[i])/2.0 for i in  range(len(clust[0].vec))]

    newcluster=bicluster(mergevec,lef=clust[lowestpair[0]],right=clust[lowestpair[1]],distance=closest,id=currentclustid)
    currentclustid-=1
    del clust[lowestpair[1]]
    del clust[lowestpair[0]]
    clust.append(newcluster)
    
    return clust[0]





