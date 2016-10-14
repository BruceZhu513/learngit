from swampy.TurtleWorld import *
from polygon import *
def square(t):
    for i in range(4):
        fd(t,100)
        lt(t)

if __name__=='__main__':
    world=TurtleWorld()
    bob=Turtle()
    radius = 100
    fd(bob, radius)
    pu(bob)
    fd(bob, radius)
    lt(bob,135)
    pd(bob)
    fd(bob, radius)
##    square(bob)
    wait_for_user()
