from numpy  import  * 
from ipdb import set_trace
import operator
from os import listdir



def classify0(inX,dataSet,labels,k):
	##set_trace() gogogogo
	dataSetSize=dataSet.shape[0]
	diffMat=tile(inX,(dataSetSize,1))-dataSet
	sqDiffMat=diffMat**2
	sqDistances=sqDiffMat.sum(axis=1)
	distances=sqDistances**0.5
	sortedDistIndicies=distances.argsort()
	classCount={}
	for i in range(k):
		voteIlabel=labels[sortedDistIndicies[i]]
		classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
	sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]

def file2matrix(filename):
	fr=open(filename)
	arrayOLines=fr.readlines()
	numberOfLines=len(arrayOLines)
	returnMat=zeros((numberOfLines,3))
	classLabelVector_t=[]
	classLabelVector=[]
	tt=[]
	index=0
	for line in arrayOLines:
		line=line.strip()
		listFromLine=line.split('\t')
		returnMat[index,:]=listFromLine[0:3]
		classLabelVector_t.append(listFromLine[-1])
		index+=1
	tt=list(set(classLabelVector_t))
	classLabelVector=[tt.index(y)+1 for y in classLabelVector_t]
	#set_trace()
	return returnMat,classLabelVector		

def autoNorm(dataSet):
	#set_trace()
	minVals=dataSet.min(0)
	maxVals=dataSet.max(0)
	ranges=maxVals-minVals
	normDataSet=zeros(shape(dataSet))
	m=dataSet.shape[0]
	normDataSet=dataSet-tile(minVals,(m,1))
	normDataSet=normDataSet/tile(ranges,(m,1))
	return normDataSet,ranges,minVals


def datingClassTest():
	#set_trace()
	hoRation=0.06
	datingDataMat,datingLabels=file2matrix('datingTestSet.txt')
	normMat,ranges,minVals=autoNorm(datingDataMat)
	m=normMat.shape[0]
	numTestVecs=int(m*hoRation)
	errorCount=0.0
	#set_trace()
	for i in range(numTestVecs):
		classifierResult=classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],5)
		print "the classifier came backe with:%d,the real answer is :%d" % (classifierResult,datingLabels[i])
		if (classifierResult!=datingLabels[i]):errorCount+=1.0
	#set_trace()
	print "the total error rate is:%f" % (errorCount/float(numTestVecs))


def img2vector(filename):
	returnVect=zeros((1,1024))
	fr=open(filename)
	for i in range(32):
		linestr=fr.readline()
		#set_trace()
		for j in range(32):
			returnVect[0,32*i+j]=int(linestr[j])
	return returnVect
		


def handwritingClassTest():
	hwLabels=[]
	trainingFileList=listdir('/home/linjun/Downloads/machinelearn/machinelearninginaction/Ch02/digits/trainingDigits')
	m=len(trainingFileList)
	trainingMat=zeros((m,1024))
	for i in range(m):
		fileNameStr=trainingFileList[i]
		fileStr=fileNameStr.split('.')[0]
		classNumStr=int(fileStr.split('_')[0])
		hwLabels.append(classNumStr)
		trainingMat[i,:]=img2vector('/home/linjun/Downloads/machinelearn/machinelearninginaction/Ch02/digits/trainingDigits/%s' % fileNameStr)
	testFileList=listdir('/home/linjun/Downloads/machinelearn/machinelearninginaction/Ch02/digits/testDigits')
	errorCount=0.0
	mTest=len(testFileList)
	for i  in range(mTest):
		fileNameStr=testFileList[i]
		fileStr=fileNameStr.split('.')[0]
		classNumStr=int(fileStr.split('_')[0])
		vectorUnderTest=img2vector('/home/linjun/Downloads/machinelearn/machinelearninginaction/Ch02/digits/testDigits/%s' % fileNameStr)
		classifierResult=classify0(vectorUnderTest,trainingMat,hwLabels,5)
		print "the classifier came back with: %d ,the real answer is: %d" % (classifierResult,classNumStr)
		if (classifierResult!=classNumStr):errorCount+=1.0
		print "\nthe total number of errors is:%d " % errorCount
		print "\nthe total error rate is :%f" % (errorCount/float(mTest))

