import math

class Point:
     """Represents a point in 2-D space."""
    

def distance_between_points(Point1,Point2):
    return Point1.x-Point2.y



if __name__=='__main__':
    Point1=Point()
    Point1.x=3
    Point1.y=4
    Point2=Point()
    Point2.x=4
    Point2.y=5
    print distance_between_points(Point1,Point2)
