from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt



def createDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return group,labels

def classify0(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]
    diffMat=tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat=diffMat**2
    sqDistances=sqDiffMat.sum(axis=1)
    distances=sqDistances**0.5
    print 'type',type(distances)
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
    classLabelVector=[]
    index=0
    for line in arrayOLines:
        line=line.strip()
        listFromLine=line.split('\t')
        returnMat[index,:]=listFromLine[:3]
        classLabelVector.append(listFromLine[-1])
        index+=1
    return returnMat,classLabelVector

def autoNorm(dataSet):
    minVals=dataSet.min(0)
    maxVals=dataSet.max(0)
    ranges=maxVals-minVals
    m=dataSet.shape[0]
    normDataSet=zeros(shape(dataSet))
    normDataSet=dataSet-tile(minVals,(m,1))
    normDataSet=normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minVals


def datingClassTest():
    hoRatio=0.1
    datingDataMat,datingLabels=file2matrix('datingTestSet2.txt')
    normMat,ranges,minVals=autoNorm(datingDataMat)
    m=normMat.shape[0]
    numTestVecs=int(m*hoRatio)
    errorCount=0.0
    for i in range(numTestVecs):
        classifierResult=classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        if (classifierResult!=datingLabels[i]):errorCount+=1
    print (errorCount/float(numTestVecs))


if __name__=='__main__':
##     group,labels=createDataSet()
##     print group
##     print labels
##
##     print classify0([0,0],group,labels,3)

##    datingDataMat,datingLabels=file2matrix('datingTestSet2.txt')
##    print datingLabels[:10]
##    normMat,ranges,minVals=autoNorm(datingDataMat)
##    print normMat[:10]
##    
##    fig=plt.figure()
##    ax=fig.add_subplot(111)
##    ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
##    plt.show()


    print datingClassTest()
