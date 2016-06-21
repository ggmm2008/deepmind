# coding=gbk

import matplotlib.pyplot as plt
from ipdb import set_trace

#�����ǶԻ�����ͼ�����Ե�һЩ���壬���Բ��ùܣ���Ҫ�Ǻ�����㷨
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")
#���ǵݹ��������Ҷ�ӽڵ�������Ƚϼ�
def getNumLeafs(myTree):
  numLeafs = 0
  firstStr = myTree.keys()[0]
  secondDict = myTree[firstStr]
  for key in secondDict.keys():
    if type(secondDict[key]).__name__=='dict':#test to see if the nodes are dictonaires, if not they are leaf nodes
      numLeafs += getNumLeafs(secondDict[key])
    else:   numLeafs +=1
  return numLeafs
#���ǵݹ����������ȣ��Ƚϼ�
def getTreeDepth(myTree):
  maxDepth = 0
  firstStr = myTree.keys()[0]
  secondDict = myTree[firstStr]
  for key in secondDict.keys():
    if type(secondDict[key]).__name__=='dict':#test to see if the nodes are dictonaires, if not they are leaf nodes
      thisDepth = 1 + getTreeDepth(secondDict[key])
    else:   thisDepth = 1
    if thisDepth > maxDepth: maxDepth = thisDepth
  return maxDepth
#���������һע����ʽ���ƽڵ�ͼ�ͷ�ߣ����Բ��ù�
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
  createPlot.ax1.annotate(nodeTxt, xy=parentPt,  xycoords='axes fraction',
       xytext=centerPt, textcoords='axes fraction',
       va="center", ha="center", bbox=nodeType, arrowprops=arrow_args )
#����������������ϵı�ע����
def plotMidText(cntrPt, parentPt, txtString):
  xMid = (parentPt[0]-cntrPt[0])/2.0 + cntrPt[0]
  yMid = (parentPt[1]-cntrPt[1])/2.0 + cntrPt[1]
  createPlot.ax1.text(xMid, yMid, txtString, va="center", ha="center", rotation=30)
#�ص㣬�ݹ飬����������ͼ�Ļ��ƣ��ѣ��Լ���Ϊ��
def plotTree(myTree, parentPt, nodeTxt):#if the first key tells you what feat was split on
  numLeafs = getNumLeafs(myTree)  #this determines the x width of this tree
  depth = getTreeDepth(myTree)
  firstStr = myTree.keys()[0]	 #the text label for this node should be this
  cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW, plotTree.yOff)
  plotMidText(cntrPt, parentPt, nodeTxt)
  plotNode(firstStr, cntrPt, parentPt, decisionNode)
  secondDict = myTree[firstStr]
  plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
  for key in secondDict.keys():
    if type(secondDict[key]).__name__=='dict':#test to see if the nodes are dictonaires, if not they are leaf nodes   
      plotTree(secondDict[key],cntrPt,str(key))		#recursion
    else:   #it's a leaf node print the leaf node
      plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
      plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
      plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
  plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD
#if you do get a dictonary you know it's a tree, and the first element will be another dict
#����������Ļ��ƣ��ϱ����߼��Ļ���
def createPlot(inTree):
  set_trace()
  fig = plt.figure(1, facecolor='white')
  fig.clf()
  axprops = dict(xticks=[], yticks=[])
  createPlot.ax1 = plt.subplot(111, frameon=False)	#no ticks
  plotTree.totalW = float(getNumLeafs(inTree))
  plotTree.totalD = float(getTreeDepth(inTree))
  plotTree.xOff = -0.5/plotTree.totalW; plotTree.yOff = 1.0;
  plotTree(inTree, (0.5,1.0), '')
  plt.show()
#����������������ݼ���������
def retrieveTree(i):
  listOfTrees =[{'no surfacing': {0:{'flippers': {0: 'no', 1: 'yes'}}, 1: {'flippers': {0: 'no', 1: 'yes'}}, 2:{'flippers': {0: 'no', 1: 'yes'}}}},
          {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}
          ]
  return listOfTrees[i]
createPlot(retrieveTree(0))