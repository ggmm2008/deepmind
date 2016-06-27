from ipdb import set_trace


def loadDataSet():
    postingList=[['my','dog','has','flea','problems','help','please'],['maybe','not','take'\
    'him','to','dog','park','stupid'],['my','dalmation','is','so','cute','I','lvoe','him'\
    ],['stop','posting','stupid','worthless','garbage'],['mr','licke','ate','my','steak','how',\
    'to','stop','him'],['quit','buying','worthless','dog','food','stupid']]
    classVec=[0,1,0,1,0,1]
    return postingList,classVec


def createVocabList(dataSet):
    #set_trace()
    vocabSet=set([])
    for document in dataSet:
        vocabSet=vocabSet|set(document)
    return list(vocabSet)


def setOfWords2Vec(vocabList,inputSet):
    set_trace()
    returnVec=[0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]=1
        else:
            print "the word:%s is not in my Vocabulary!" % word
    return returnVec