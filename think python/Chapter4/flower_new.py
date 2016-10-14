try:
    from swampy.TurtleWorld import *
except ImportError:
    from TurtleWorld import *

from polygon import *


def petal(t,r,angle):
    for i in range(2):
        arc(t,r,angle)
        lt(t,180-angle)

def flower(t,r,angle,n):
    for i in range(n):
        petal(t,r,angle)
        lt(t,360/n)

def move(t,length):
    pu(t)
    fd(t,length)
    pd(t)

    
if __name__=="__main__":
    wrold =TurtleWorld()
    bob=Turtle()
    bob.delay=0.01
    move(bob,-100)
    
##    petal(bob,40,40)
    flower(bob,80,20,7)
##    die(bob)
    wait_for_user()
