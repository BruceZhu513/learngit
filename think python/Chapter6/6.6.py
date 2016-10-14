def is_palindrome(word):
    length=len(word)
    for i in range(length/2):
        if word[i]!=word[length-1-i]:
            return False
    return True

if __name__=='__main__':
    print is_palindrome('abba')
