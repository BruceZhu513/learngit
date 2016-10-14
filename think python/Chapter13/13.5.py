import random


def histogram(t):
    res=dict()
    for a in t:
        res[a]=res.get(a,0)+1
    return res

def choose_from_hist():
    

if __name__=='__main__':
    t=['a','a','b']
    hist=histogram(t)
    print hist
    
