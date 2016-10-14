from swampy.World import World


class Rectangle():
    'waitting'
class Circle():
    'waitting'


def draw_rectangle(canvas,rect):
    canvas.rectangle(rect.bbox,fill=rect.color)


def draw_circle(canvas,circle):
    canvas.circle(circle.centre,circle.radiums,fill=circle.color)

def draw_Czekh(canvas,points):
    rect=Rectangle()
    rect1=Rectangle()
    rect.bbox=[[-150,-100],[150,100]]
    rect.color='white'
    rect1.bbox=[[-150,-100],[150,0]]
    rect1.color='red'
    draw_rectangle(canvas,rect)
    draw_rectangle(canvas,rect1)
    canvas.polygon(points,fill='blue')
    
if __name__=='__main__':
    world=World()
    canvas=world.ca(width=500,height=500,background='white')
##
##    rect=Rectangle()
##    rect.bbox=[[-150,-100],[150,100]]
##    rect.color='green'
##    draw_rectangle(canvas,rect)
##
##
##    circle=Circle()
##    circle.centre=[25,0]
##    circle.radiums=70
##    circle.color='red'
##    draw_circle(canvas,circle)
##    canvas.circle([-25,0],70,outline=None,fill='red')
    points=[[-150,100],[-150,-100],[0,0]]
    draw_Czekh(canvas,points)

    
    world.mainloop()
