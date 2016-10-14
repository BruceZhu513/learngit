def gcd(a,b):
    if b==0:
        return a
    r=a%b
    print r
    return gcd(b,r)

if __name__=='__main__':
    print gcd(8,3)
