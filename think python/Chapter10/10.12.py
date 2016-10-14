import bisect

def read_files(filename):
    res=[]
    with open(filename) as f:
        for letter in f.readlines():
            letter=letter.strip()
            res.append(letter)
    return res

def is_reverse(word):
    return word==word[::-1]

def reverse_pair(words):
    res=[]
    for word in words:
        index=bisect.bisect_left(words,word)
        index_reverse=bisect.bisect_left(words,word[::-1])
        if index_reverse<len(words) and index!=index_reverse and words[index_reverse]==word[::-1]:
            print word,word[::-1]
    return res

if __name__=='__main__':
    words=[]
    pairs=[]
    words_test=['aa','bus','morining','peels','sleep','sloop','sub']
    words=read_files('words.txt') 
    paris=reverse_pair(words)
##    print bisect.bisect_left(words_test,'sloop')
    print pairs
