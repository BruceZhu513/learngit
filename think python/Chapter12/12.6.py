from readfiles import read_file

def extract_word(word,words):
    new_words=[]
    for i in range(len(word)):
        new_word=word[0:i]+word[i+1:]
        if new_word in words:
            if new_word!=' ':
                new_words.append(new_word)
    return new_words

if __name__=='__main__':
    words=read_file('E:\PostGraduate\python project\\think python\Chapter10\words1.txt')
    for word in words:
        print extract_word(word,words)
