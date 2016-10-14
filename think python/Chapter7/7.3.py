import math
global epsilon
epsilon=0.0000001

def square_root(a,x):
    y=0.0
    while True:
        y=(x+a/x)/2
        if abs(y-x)<=epsilon:
            return y
        x=y

if __name__=='__main__':
    print square_root(8.0,3.0)
    print math.sqrt(8.0)
    print square_root(8.0,3.0)-math.sqrt(8.0)
