import numpy as np
from ipdb import set_trace


def loadDataSet():
    dataMat=[]
    labelMat=[]
    fr=open('testSet.txt')
    for line in fr.readlines():
        lineArr=line.strip().split()
        dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat


def sigmoid(inX):
    return 1.0/(1+np.exp(-inX))


def gradAscent(dataMatIn,classLabels):
    dataMatrix=np.mat(dataMatIn)
    labelMat=np.mat(classLabels).transpose()
    m,n=np.shape(dataMatrix)
    alpha=0.001
    maxCycles=500
    weights=np.ones((n,1))
    set_trace()
    for k in range(maxCycles):
        h=sigmoid(dataMatrix*weights)
        error=(labelMat-h)
        weights=weights+alpha*dataMatrix.transpose()*error
    #set_trace()
    return weights



def plotBestFit(weights):
    import matplotlib.pyplot as plt
    
    dataMat,labelMat=loadDataSet()
    dataArr=np.array(dataMat)
    n=np.shape(dataArr)[0]
    xcord1=[];ycord1=[]
    xcord2=[];ycord2=[]
    for i in range(n):
        if int(labelMat[i])==1:
            xcord1.append(dataArr[i,1]);ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]);ycord2.append(dataArr[i,2])
    fig=plt.figure()
    
    ax=fig.add_subplot(111)
    ax.scatter(xcord1,ycord1,s=30,c='red',marker='s')
    ax.scatter(xcord2,ycord2,s=30,c='green')
    #set_trace()################
    x=np.arange(-3.0,3.0,0.1)
    y=np.array((-weights[0]-weights[1]*x)/weights[2])[0]
    ax=plt.plot(x,y)
    plt.xlabel('x1');plt.ylabel('x2');
    plt.show()


def stocGradAscent0(dataMatrix,classLabels):
    m,n=np.shape(dataMatrix)
    alpha=0.01
    weights=np.ones(n)
    xPlot=np.zeros((m,4))
    #set_trace()##################
    for i in range(m):
        hd=sigmoid(sum(dataMatrix[i]*weights))
        error=classLabels[i]-hd
        weights=weights+list(alpha*error*np.array(dataMatrix[i])) #nainaide 
        #set_trace()####################
        xPlot[i][1:4]=weights
        xPlot[i][0]=i
    return weights,xPlot


def stocGradAscent2(dataMatrix,classLabels,numIter=250):
    m,n=np.shape(dataMatrix)
    #alpha=0.01
    weights=np.ones(n)
    xPlot=np.zeros((numIter,4))
    #set_trace()###################
    for jd in range(numIter): 
        dataIndex=range(m)
        for i in range(m):
            alpha=4/(1.0+jd+i)+0.02
            randIndex=int(np.random.uniform(0,len(dataIndex)))
            #print '%s/%s,%s/%s,randIndex=%s' % (str(jd),str(numIter),str(i),str(m),str(randIndex))+'\n'
            hd=sigmoid(sum(dataMatrix[randIndex]*weights))
            error=classLabels[randIndex]-hd
            weights=weights+list(alpha*error*np.array(dataMatrix[randIndex]))
            del(dataIndex[randIndex])
        xPlot[jd][1:4]=weights
        xPlot[jd][0]=jd           
    return weights,xPlot


def plotdiedai(xPlot):
    import matplotlib.pyplot as plt
    import pandas as pd   
   
    #x0/x1   
    fig=plt.figure() 
    ax=fig.add_subplot(111)
    #set_trace()################
    x=(pd.DataFrame(xPlot)).ix[:,0]
    y=(pd.DataFrame(xPlot)).ix[:,1]
    ax.scatter(x,y,s=30,c='green')
    ax=plt.plot(x,y)    
    plt.xlabel('x0');plt.ylabel('x1');
    plt.show()

    #x0/x2
    fig=plt.figure() 
    ax=fig.add_subplot(111)
    #set_trace()################
    x=(pd.DataFrame(xPlot)).ix[:,0]
    y=(pd.DataFrame(xPlot)).ix[:,2]
    ax.scatter(x,y,s=30,c='green')
    ax=plt.plot(x,y)    
    plt.xlabel('x0');plt.ylabel('x2');
    plt.show()

    #x0/x3
    fig=plt.figure() 
    ax=fig.add_subplot(111)
    #set_trace()################
    x=(pd.DataFrame(xPlot)).ix[:,0]
    y=(pd.DataFrame(xPlot)).ix[:,3]
    ax.scatter(x,y,s=30,c='green')
    ax=plt.plot(x,y)    
    plt.xlabel('x0');plt.ylabel('x3');
    plt.show()