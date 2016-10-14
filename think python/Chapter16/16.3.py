class Time():
    'attr:seconds,minutes,hours'

def increment_modifier(start,seconds):
    minute = seconds/60
    start.second+=seconds/60
    if start.second>=60:
        start.minute+=1
    start.minute+=minute

    hour=start.minute/60
    start.minute=start.minute%60
    if start.minute>=60:
        start.hour+=1
        
    start.hour+=hour
    if start.hour>=24:
        start.hour-=24

    return start

def increment_prototype():
    pass

def print_time(time):
    print '%.2d:%.2d:%.2d'%(time.hour,time.minute,time.second)


if __name__=='__main__':
    start=Time()
    start.hour=9
    start.minute=55
    start.second=0

    seconds=361
    
    print_time(increment_modifier(start,seconds))
