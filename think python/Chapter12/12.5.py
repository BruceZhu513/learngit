from readfiles import read_file

def the_key(word):
    letters=[]
    for letter in word:
        letters.append(letter)
    letters.sort()
    return tuple(letters)
    
def anagram_all(words):
    res=dict()
    for word in words:
        key=the_key(word)
        if key not in res.keys():
            res[key]=[word]
        else:
            res[key].append(word)
    return res

def is_compare(word1,word2):
    count=0
    for x,y in zip(word1,word2):
        if x!=y:
            count+=1
    if count<=2:
        return True
    else:
        return False

def metathesis(anagrams):
    res=[]
    for key,values in anagrams.items():
        for i in range(len(values)/2):
            for j in range(i+1,len(values)):
                if is_compare(values[i],values[j]):
                    t=[values[i],values[j]]
                    res.append(tuple(t))
    return res
    
if __name__=='__main__':
    words=read_file('E:\PostGraduate\python project\\think python\Chapter10\words1.txt')
    anagrams=anagram_all(words)
##    for key,value in anagrams.items():
##        print key,value
    print metathesis(anagrams)

