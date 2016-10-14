from Time1 import *

def mul_time(time,factor):
    assert valid_time(time)
    return int_to_time(time_to_int(time)*factor)


if __name__=='__main__':
    start=Time()
    start.hour=1
    start.minute=20
    start.second=35

    print_time(mul_time(start,2))
