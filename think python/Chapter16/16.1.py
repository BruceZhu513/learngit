class Time():
    'attr:hour,minute,second'

def print_time(time):
    print '%.2d:%.2d:%.2d'%(time.hour,time.minute,time.second)


def is_after(time1,time2):
    return (time1.hour,time1.minute,time1.second)>(time2.hour,time2.minute,time2.second)


if __name__=='__main__':
    time1=Time()
    time1.hour=1
    time1.minute=59
    time1.second=30
    print_time(time1)

    time2=Time()
    time2.hour=1
    time2.minute=58
    time2.second=40

    print is_after(time1,time2)
