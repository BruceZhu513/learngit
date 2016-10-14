

class Time():
    'attr:seconds,minutes,hours'

def time_to_int(start):
    seconds=3600*start.hour+60*start.minute+start.second
    return seconds

def int_to_time(s):
    res=Time()
    (res.minute,res.second)=divmod(s,60)
    (res.hour,res.minute)=divmod(res.minute,60)
    return res

def increment(seconds,second):

    return seconds+second

def valid_time(time):
    if time.hour<0 or time.minute<0 or time.second <0:
        raise ValueError ,'wrong'


def print_time(time):
    print '%.2d:%.2d:%.2d'%(time.hour,time.minute,time.second)


if __name__=='__main__':
    start=Time()
    start.hour=9
    start.minute=55
    start.second=-2
    valid_time(start)
##
##    seconds=time_to_int(start)
##    second=61
##    s=increment(seconds,second)
##    end=int_to_time(s)
    
    print_time(end)
