import string
import random
from operator import itemgetter
import sys
sys.path.append('E:\PostGraduate\python project\\think python\Chapter12')
print sys.path
import readfiles
##*END*THE SMALL PRINT!
def read_file(filename,flag):
    res=[]
##  describe whether header is over
    with open(filename) as f:
        for line in f.readlines():
            if flag==1:
                res.append(line.split())
            if judge_header(line):
                flag=1
    return res


def judge_header(line):
    if line.startswith('*END*THE SMALL PRINT!'):
        return True
    return False

def calculate_words(words):
    res=dict()
    count_all=0
    for line in words:
        for word in line:
            word=word.lower().translate(None,string.punctuation+string.whitespace)
            count_all+=1
            res[word]=res.get(word,0)+1
    return count_all,res


def highFrequence_word(dic_words):
    res=[]
    top=20
    temp=sorted(dic_words.items(),key=itemgetter(1),reverse=True)
    for i in range(20):
        res.append(temp[i][0])
    return res
##not in table
def notintable(dic_words,words_table):
    res=[]
    for key in dic_words:
       if key not in words_table:
           res.append(key)
    return res

if __name__=='__main__':
    words=read_file('emma.txt')
    count_all,dic_words=calculate_words(words)
    print 'total words:%d'%count_all
    print 'number of different words:%d'%len(dic_words)
##    13.3
    high_words=highFrequence_word(dic_words)
    for high_word in high_words[0:10]:
        print '%s:%d'%(high_word,dic_words[high_word])


##13.4
    words_table=readfiles.read_file('words.txt')
    no=notintable(dic_words,words_table)
    
