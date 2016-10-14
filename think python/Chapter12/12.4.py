from readfiles import read_file
from operator import itemgetter

def define_key(words):
    l=list(words)
    key=sorted(l)
    return tuple(key)

def anagram_all(words):
    d=dict()
    for word in words:
        key=define_key(word)
        if key not in d.keys():
            d[key]=[word]
        else:
            d[key].append(word)
##        d[key]=(d.get(key,[])).append(word)
    return d

def find_maxAnagram(d):
    t=[]
    for values in d.values():
        t.append((len(values),values))
    t=sorted(t,key=itemgetter(0),reverse=True)
    return t

if __name__=='__main__':
    words=read_file('E:\PostGraduate\python project\\think python\Chapter10\words1.txt')
##    for word in words:
##        print word
    
    d=anagram_all(words)
    maxAnagram=find_maxAnagram(d)
    for i in range(len(maxAnagram)):
        print maxAnagram[i][1:]
##    for key,values in d.items():
##        print key , values
