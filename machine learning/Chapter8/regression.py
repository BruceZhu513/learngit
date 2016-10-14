from numpy import *

def loadDataSet(fileName):
    numFeat=len(open(fileName).readline().split('\t')) - 1
    dataMat=[];labelMat=[]
    fr=open(fileName)
    for line in fr.readlines():
        lineArr=[]
        curLine=line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat

def standRegress(xArr,yArr):
    xMat=mat(xArr);yMat=mat(yArr).T
    xTx=xMat.T*xMat
    if linalg.det(xTx)==0.0:
        print 'This matrix is singular,cannot do inverse'
        return
    ws =xTx.I*xMat.T*yMat
    return ws

def lwlr(testPoint,xArr,yArr,k=1.0):
    xMat=mat(xArr);yMat=mat(yArr).T
    print shape(xMat)
    m=shape(xMat)[0]
    weights=mat(eye((m)))
    for j in range(m):
        diffMat=testPoint-xMat[j,:]
        weights[j,j]=exp(diffMat*diffMat.T/(-2.0*k**2))
    xTx=xMat.T*weights*xMat
    print shape(xTx)
    if linalg.det(xTx)==0.0:
        print 'This matrix is singular,cannot do inverse'
        return
    ws=xTx.I*xMat.T*weights*yMat
    print shape(ws)
    return testPoint*ws

def lwlrTest(testArr,xArr,yArr,k=1.0):
    m=shape(testArr)[0]
    yHat=zeros(m)
    for i in range(m):
        yHat[i]=lwlr(testArr[i],xArr,yArr,k)
    return yHat

def ridgeRegress(xMat,yMat,lam=0.2):
    xTx=xMat.T*xMat
    demon=xTx+eye(shape(xMat)[1])*lam


if __name__ == '__main__':
    xArr,yArr=loadDataSet('ex0.txt')
    print xArr[:2]
    print lwlr(xArr[0],xArr,yArr,1.0)

    xMat=mat(xArr)
    strInd=xMat[:,1].argsort(0)
    print strInd
    xSort=xMat[strInd]
    print xSort
