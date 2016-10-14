from swampy.TurtleWorld import *
import math

def square(t,length=100):
    for i in range(4):
        fd(bob,100)
        lt(bob)
    print bob


def polygon(t,n,length):
    angle=360/n
    polyline(t,n,length,angle)

def polyline(t,n,length,angle):
    for i in range(n):
        fd(bob,length)
        lt(bob,angle)
    print bob

def circle(t,r):
    arc(t,r,360)

def arc(t,r,angle):
    arc_length=2*math.pi*r*angle/360
    n=int(arc_length/3)+1
    step_length=arc_length/n
    step_angle=float(angle)/n
    polyline(t,r,step_length,step_angle)

    
if __name__=='__main__':
    world=TurtleWorld()
    bob=Turtle()
    bob.delay=0.01
    n=6
    length=1
    radius=20
    angle=180
##    square(bob,length)
##    polygon(bob,n,length)
    arc(bob,radius,angle)
    wait_for_user()


