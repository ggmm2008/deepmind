import numpy as np


def loadDataSet(fileName):
    dataMat=[];labelMat=[]
    fr=open(fileName)
    for line in fr.readlines():
        lineArr=line.strip().split('\t')
        dataMat.append([float(lineArr[0]),float(lineArr[1])])
        labelMat.append(float(lineArr[2]))


def selectJrand(i,m):
    j=i
    while(j==i):
        j=int(np.random.uniform(0,m))
    return j


def clipAlpha(aj,H,L):
    if aj>H:
        aj=H
    IF L>aj:
        aj=L
    return aj
