def print_n(s,n):
    if n<=0:
        return
    print s
    print_n(s,n-1)

def test():
    print 'enheng'
def do_n(f,n):
    if n<=0:
        return
    f()
    do_n(f,n-1)

if __name__=='__main__':
##    print_n('hello',2)
    do_n(test,4)
