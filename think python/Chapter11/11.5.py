def histogram(words):
    d=dict()
    for letter in words:
        d[letter]=d.get(letter,0)
        d[letter]+=1
    return d


##def invert_dict(d):
##    inverse=dict()
##    for key in d:
##        val=d[key]
##        if val not in inverse:
##            inverse[val]=[key]
##        else:
##            inverse[val].append(key)
##    return inverse

def invert_dict(d):
    inverse={}
    for key,val in d.iteritems():
        inverse.setdefault(val,[]).append(key)
    return inverse

hist=histogram('parrot')
print hist
inverse=invert_dict(hist)
print inverse
