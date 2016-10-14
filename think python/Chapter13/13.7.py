from hu import read_file,calculate_words
import bisect
import random

def random_word(dic_words):
    d=dict()
    pre,i=0,0
    all_words=[]
    ##  a random number
    for key in dic_words.keys():
        cur=pre+dic_words[key]
    ##        print key,cur
        d[i]=key
        all_words.append(cur)
        pre=cur
        i+=1
    n=random.randint(all_words[0],all_words[-1])
    index=bisect.bisect_left(all_words,n)
    print n,index,all_words[index]
    return d[index]

if __name__=='__main__':
    words=read_file('emma.txt')
    count_all,dic_words=calculate_words(words)




    print random_word(dic_words)

    
##        print '%s:%d'%(key,dic_words[key])

##    print all_words   
    
