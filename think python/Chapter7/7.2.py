global epsilon
epsilon=0.0000001

def square_root(a,x):
    y=0.0
    while True:
        y=(x+a/x)/2
        print y
        if abs(y-x)<=epsilon:
            return y
        x=y
    
if __name__=='__main__':
    print square_root(8.0,3.0)
