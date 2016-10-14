from numpy import mat,matrix,array,shape,ones,exp,dot,arange
import random
def loadDataSet():
    dataMat=[];labelMat=[]
    fr=open('testSet.txt')
    for line in fr.readlines():
        lineArr=line.strip().split()
        dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

def sigmoid(inX):
    return 1.0/(1+exp(-inX))

def gradAscent(dataMatIn,classLabels):
    dataMatrix=mat(dataMatIn)
    labelMat=mat(classLabels).transpose()
    m,n=shape(dataMatrix)
    alpha=0.001
    maxCycles=500
    weights=ones((n,1))
    for k in range(maxCycles):
        h=sigmoid(dataMatrix*weights)
##        print shape(dataMatrix*weights)
##        print shape(h)
        error=(labelMat-h)
##        print shape(error)
        weights=weights+alpha*dataMatrix.transpose()*error
##        print shape(weights)
    return weights

def stocGradAscent0(dataMatrix, classLabels):
    m,n = shape(dataMatrix)
    alpha = 0.01
    weights = ones(n)   #initialize to all ones
    for i in range(m):
##        print shape(weights*mat(dataMatrix[i]).T)
        h = sigmoid(weights*mat(dataMatrix[i]).T)
##        h = sigmoid(sum(dataMatrix[i]*weights))
        error = classLabels[i] - h
        error=array(error)
##        print shape(error)
        weights = weights + alpha * error * array(dataMatrix[i])
    return weights

def stocGradAscent1(dataMatrix,classLabels,numIter=150):
    m,n=shape(dataMatrix)
    weights=ones(n)
    for j in range(numIter):
        dataIndex=range(m)
        for i in range(m):
            alpha=4/(1.0+i+j)+0.01
            index=int(random.uniform(0,len(dataIndex)))
            h=sigmoid(weights*mat(dataMatrix[index]).T)
            error=classLabels[index]-h
            weights = weights + alpha * error * array(dataMatrix[i])
##            print dataIndex[index]
            del dataIndex[index]
    return weights

def plotBestFit(weights):
    import matplotlib.pyplot as plt
    dataMat,labelMat=loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0] 
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i])== 1:
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x, y)
    plt.xlabel('X1'); plt.ylabel('X2');
    plt.show()
    
def classifyVector(inX,weights):
    prob=sigmoid(sum(inX*weights))
    if prob>0.5:
        return 1.0
    else:
        return 0.0

def colicTest():
    

if __name__=='__main__':
    dataArr,labelMat=loadDataSet()
    weights=gradAscent(dataArr,labelMat)
##    print stocGradAscent0(dataArr,labelMat)
    weights=stocGradAscent1(dataArr,labelMat)
    plotBestFit(weights)
