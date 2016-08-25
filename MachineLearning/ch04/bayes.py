# -*- coding:utf-8 -*-  
#===============================
#  
#+==============================



from ipdb import set_trace
import numpy as np


def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec
                 
def createVocabList(dataSet):
    vocabSet = set([])  #create empty set
    for document in dataSet:
        vocabSet = vocabSet | set(document) #union of the two sets
    return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
    #set_trace()
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print "the word: %s is not in my Vocabulary!" % word
    return returnVec


def bagOfWords2Vec(vocabList, inputSet):
    #set_trace()
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
        else: print "the word: %s is not in my Vocabulary!" % word
    return returnVec


def trainNB0(trainMatrix,trainCategory):
    #set_trace()
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = np.ones(numWords); p1Num = np.ones(numWords)      #change to ones() 
    p0Denom = 2.0; p1Denom = 2.0                        #change to 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            #set_trace()
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    #set_trace()
    p1Vect = np.log(p1Num/p1Denom)         #change to log()
    p0Vect = np.log(p0Num/p0Denom)        #change to log()
    return p0Vect,p1Vect,pAbusive


def listVec(vocabList,inputSet):
    trainMat=[]
    for postinDoc in inputSet:
        trainMat.append(setOfWords2Vec(vocabList,postinDoc))
    return trainMat

def classifyNb(vec2Classify,p0Vec,p1Vec,pClass1):
    p1=sum(vec2Classify*p1Vec)+np.log(pClass1)
    p0=sum(vec2Classify*p0Vec)+np.log(1-pClass1)
    if p1>p0:
        return 1
    else:
        return 0


def testingNB():
    dataSet,listClasses=loadDataSet()
    myVocabList=createVocabList(dataSet)
    trainMat=[]
    for line in dataSet:
        trainMat.append(setOfWords2Vec(myVocabList,line))
    p0V,p1V,pAb=trainNB0(trainMat,listClasses)
    testEntry=['love','my','dalmation']
    thisDoc=np.array(setOfWords2Vec(myVocabList,testEntry))
    print testEntry,'classifyed as :',classifyNb(thisDoc,p0V,p1V,pAb)
    testEntry=['stupid','garbage']
    thisDoc=np.array(setOfWords2Vec(myVocabList,testEntry))
    print testEntry,'classifyed as :',classifyNb(thisDoc,p0V,p1V,pAb)