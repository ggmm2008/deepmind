import numpy as np


def loadDataSet(fileName):
    dataMat=[];labelMat=[]
    fr=open(fileName)
    for line in fr.readlines():
        lineArr=line.strip().split('\t')
        dataMat.append([float(lineArr[0]),float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat,labelMat


def selectJrand(i,m):
    j=i
    while(j==i):
        j=int(np.random.uniform(0,m))
    return j


def clipAlpha(aj,H,L):
    if aj>H:
        aj=H
    if L>aj:
        aj=L
    return aj


def smoSimple(dataMatIn,classLabels,C,toler,maxIter):
    dataMatrix=np.mat(dataMatIn);labelMat=np.mat(classLabels).transpose()
    b=0;m,n=shape(dataMatrix)
    alphas=np.mat(np.zeros((m,1)))
    iter=0
    while(iter<maxIter):
        alphaPairsChanged=0
        for i in range(m):
            fxi=float(multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[i,:].T))+b
            Ei=fXi-float(labelMat[i])
            alphaIold=alphas[i].copy();
            alphaJold=alphas[j].copy();
            if(labelMat[i]!=labelMat[j]):
                L=max(0,alphas[j]-alphas[i])
                H=min(C,C+alphas[j]-alphas[i])