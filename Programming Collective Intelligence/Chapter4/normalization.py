scores={'a':1.0,'b':2.0,'c':3.0,'d':4.0,'e':5.0}

res=dict([(i,score/5.0) for (i,score) in scores.items()])
print res
