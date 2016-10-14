# -*- coding: utf-8 -*-
import numpy as np
import scipy as sp
import pickle
from sklearn import tree
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split

data=[]
labels=[]
with open('1.txt') as ifile:
    for line in ifile:
        tokens=line.strip().split(' ')
        data.append([float(tk) for tk in tokens[:-1]])
        labels.append(tokens[-1])
x=np.array(data)
labels=np.array(labels)
y=np.zeros(labels.shape)

##两个array合并行程新的
##print y
y[labels=='fat']=1
##print y
##自己的
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
clf=tree.DecisionTreeClassifier(criterion='entropy')
decision_tree=clf.fit(x_train,y_train)
with open('tree','w') as f:
    pickle.dump(decision_tree,f)

print clf.feature_importances_

answer=clf.predict(x_train)
print x_train
print answer
print y_train
print np.mean(answer==y_train)

precision,recall,thresholds=precision_recall_curve(y_train,clf.predict(x_train))
print clf.predict_proba(x)
print y
print clf.predict_proba(x)[:,1]
answer=clf.predict(x)
print answer
print classification_report(y,answer,target_names=['thin','fat'])

