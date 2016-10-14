import time
def old_fib(n):
    if n==1 or n==0:
        return 1
    else:
        return old_fib(n-1)+old_fib(n-2)

def new_fib(n):
    know={'0':1,'1':1}
    if n in know:
        return know[n]
    
    if n==1 or n==0:
        return 1
    else:
        res=old_fib(n-1)+old_fib(n-2)
        know[n]=res
        return res

if __name__=='__main__':
    s=time.clock()
    print old_fib(11)
    e=time.clock()
    print e-s

    s=time.clock()
    print new_fib(11)
    e=time.clock()
    print e-s
