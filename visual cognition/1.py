# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

##img=cv2.imread('1.jpg',0)
##print img.shape

##==============calc Hist=============
#### hist is a 256*1 array
##[256] bin's range  [0,256] pixes'range
##hist=cv2.calcHist([img],[0],None,[256],[0,256])
###img.ravel() transfer img to 1-d array
##hist,bins=np.histogram(img.ravel(),256,[0,256])
##hist=np.bincount(img.ravel(),minlength=256)

##==============draw Hist=============
##plt.hist(img.ravel(),256,[0,128])
##plt.show()

##img=cv2.imread('1.jpg')
####bgr responded to [0][1][2] 
##color=('b','g','r')
##for i,col in enumerate(color):
##    histr=cv2.calcHist([img],[i],None,[256],[0,256])
##    plt.plot(histr)
##    plt.xlim([0,256])
##plt.show()


##==============use Mask=============
#create a mask,copy img.shape[:2]==img.shape
##mask = np.zeros(img.shape,np.uint8)
##mask[50:180,0:100]=255
##masked_img=cv2.bitwise_and(img,img,mask=mask)
##
####cal histogram with mask and without mask
##hist_full=cv2.calcHist([img],[0],None,[256],[0,256])
##hist_mask=cv2.calcHist([img],[0],mask,[256],[0,256])
##
##plt.subplot(221),plt.imshow(img,'gray')
##plt.subplot(222),plt.imshow(mask,'gray')
##plt.subplot(223),plt.imshow(masked_img,'gray')
##plt.subplot(224),plt.plot(hist_full),plt.plot(hist_mask)
##plt.xlim([0,256])
##
##plt.show()

##==============use  useless=============
##hist,bins=np.histogram(img.flatter(),256,[0,256])
##cdf=hist.cumsum()
##cdf_normalized=cdf*hist.max()/cdf.max()
##
##plt.plot(cdf_normalized,color='b'))
##plt.hist(img.flatten(),256,[]0,256,color='r')
##plt.xlim([0,256])


##==============equalize Hist=============
##equ=cv2.equalizeHist(img)
##print equ.shape
##res=np.hstack((img,equ))
##print img
##print equ
##print res
##cv2.imwrite('res.png',res)

##clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
##cl1=clahe.apply(img)
##res=np.hstack((img,cl1))
##cv2.imwrite('clahe_2.jpg',res)

##==============draw 2d Hist=============
##BGR2HSV
##img=cv2.imread('1.jpg')
##print img.shape
##hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
##hist=cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
##hist,xbins,ybins=np.histogram2d(h.ravel(),s.ravel(),[180,256],[[0,180],[0,256]])
##plt.imshow(hist,interpolation='nearest')
##plt.show()

##==============backProject Hist=============
##roi=cv2.imread('1.jpg')
##hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
####print hsv
##
##target=cv2.imread('2.jpg')
##hsvt=cv2.cvtColor(target,cv2.COLOR_BGR2HSV)
####print hsvt
##
### calculating object histogram
##roihist=cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
##roihist=cv2.calcHist([hsvt],[0,1],None,[180,256],[0,180,0,256])
####print roihist
### normalize histogram and apply backprojection
### 归一化：原始图像，结果图像，映射到结果图像中的最小值，最大值，归一化类型
###cv2.NORM_MINMAX 对数组的所有值进行转化，使它们线性映射到最小值和最大值之间
### 归一化之后的直方图便于显示，归一化之后就成了0 到255 之间的数了。
##cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
####print roihist
####返回一个概率图像
##dst=cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)
##print dst
##
### Now convolute with circular disc
### 此处卷积可以把分散的点连在一起
##disc=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
##dst=cv2.filter2D(dst,-1,disc)
##
####返回的结果是一个概率图像，我们再使用一个圆盘形卷积核对其做卷操作，最后使用阈值进行二值
##ret,thresh=cv2.threshold(dst,50,255,0)
### 别忘了是三通道图像，因此这里使用merge 变成3 通道
##thresh=cv2.merge((thresh,thresh,thresh))
### 按位操作
##res=cv2.bitwise_and(target,thresh)
##
##res=np.hstack((target,thresh,res))
##cv2.imwrite('res2.jpg',res)
##cv2.imshow('l',res)
##cv2.waitKey(0)
####

##==============backProject Hist(try)=============
im=cv2.imread('1.jpg')
hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)

hist=cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
cv2.normalize(hist,hist,0,255,cv2.NORM_MINMAX)
res=cv2.calcBackProject([hsv],[0,1],hist,[0,180,0,256],1)
disc=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
res=cv2.filter2D(res,-1,disc)

cv2.imshow("Original Image", im)
cv2.imshow("Original hist", hist)
cv2.imshow("BackProjected", res)
cv2.waitKey(0) 
