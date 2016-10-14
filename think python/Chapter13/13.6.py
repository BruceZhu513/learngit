from hu import read_file,calculate_words
import bisect
import random


def subtract(dic_words,words_table):
    return set(words_table)-set(dic_words)


if __name__=='__main__':
    words=read_file('emma.txt',0)
    count_all,dic_words=calculate_words(words)

    words_table=read_file('E:\PostGraduate\python project\\think python\Chapter10\words.txt',1)
    count_all,words_table=calculate_words(words_table)
    print 
    print words[:20]

    a=subtract(dic_words,words_table)
    for b in a:
        print b,
    
