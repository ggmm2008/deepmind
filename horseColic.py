import pandas as pd
from ipdb import set_trace
import numpy as np

def sigmoid(inX):
    #set_trace()
    return 1.0/(1+np.exp(-inX))


def classifyVector(inX,weights):
    #set_trace()
    prob=sigmoid(sum(inX*weights))
    if prob>0.5:
        return 1.0
    else:
        return 0.0


def stocGradAscent22(dataMatrix,classLabels,numIter):
    #set_trace()
    m,n=np.shape(dataMatrix)
    #alpha=0.01
    weights=np.ones(n)
    #xPlot=np.zeros((numIter,4))
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
        #xPlot[jd][1:4]=weights
        #xPlot[jd][0]=jd           
    return weights



def colicTest():
    frTrain=pd.read_table('horseColicTraining.txt',sep='\t',header=None)
    frTest=pd.read_table('horseColicTest.txt',sep='\t',header=None)
    #set_trace()##########################
    t1=(frTrain.ix[:,0:21]).values.tolist()
    t2=(frTrain.ix[:,21]).values.tolist()
    trainWeghts=stocGradAscent22(t1,t2,600)
    errorCount=0;numTestVec=len(frTest)
    culine=[]
    #set_trace()##########################
    for i in range(numTestVec):
        culine=frTest.ix[i]
        t3=int(classifyVector(culine,trainWeghts))
        t4=frTest.ix[i,21]
        print "no:%d:classifyVector :%d,frTestix:%d" % (i,t3,t4)
        print "\n"
        if t3!=t4:
            errorCount+=1
    #set_trace()##############################
    errorRate=(float(errorCount)/numTestVec)
    print "the error rate of this test is : %f" % errorRate
    return errorRate

    