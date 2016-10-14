from anagram_sets import *
import pickle
import sys

def store_anagrams(filename,ad):
    filename=pickle.dumps(ad)
    print 'a'
    return filename

def read_anagrams(filename):
    print 'b'
    return pickle.loads(filename)

if __name__ == '__main__':
        ad=all_anagrams('E:\PostGraduate\python project\\think python\Chapter10\words1.txt')
        filename=store_anagrams('anagrams.db',ad)
        print read_anagrams(filename)
