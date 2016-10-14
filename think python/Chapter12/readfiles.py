def read_file(filename):
    res=[]
    with open(filename) as f:
        for word in f.readlines():
            word=word.strip()
            res.append(word)
    return res

if __name__=='__main__':
    words=read_file('E:\PostGraduate\python project\\think python\Chapter10\words.txt')
    for word in words:
        print word
    
