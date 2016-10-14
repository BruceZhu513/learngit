import bisect

def read_file(filename):
    res=[]
    with open(filename) as f.readlines():
        for word in f:
            word=word.strip()
            res.append(word)
    return res

def is_exists(word_list,word):
    index=bisect.bisect_left(word_list,word)
    if word_list[index]==word:
        return True
    return False

def find_pairs(word_list):
    for word in word_list:
        if is_exists(word_list,word[::2]) and is_exists(word_list,word[1::2]):
            print word,word[::2],word[1::2]
        


if __name__=='__main__':
    word_list=[]
    word_list=read_files('words.txt')
    find_pairs(word_list)
