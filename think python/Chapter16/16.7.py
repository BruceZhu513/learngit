import time
from datetime import datetime


def cacl_birth(birth):
    print (datetime.today()-birth).days

def days_until_birthday(birthday):
    today=datetime.today()
    now_birth=datetime(datetime.today().year,birthday.month,birthday.day)
    if today<now_birth:
        next_birth=now_birth
    else:
        next_birth=datetime(datetime.today().year+1,birthday.month,birthday.day)

    print next_birth
    return next_birth-today

def double_day(b1, b2):
    """Compute the day when one person is twice as old as the other.

    b1: datetime birthday of the younger person
    b2: datetime birthday of the older person
    """
    assert b1 > b2
    delta = b1 - b2
    double_day = b1 + delta
    return double_day

if __name__=='__main__':
##    print datetime.today()
##    print datetime.fromtimestamp(time.time())
##    print datetime.min
##    print datetime.max
##    print datetime.now()
##    print datetime.utcnow()
##    print date.resolution
##    print datetime.isoweekday(datetime.today())
##    print datetime.isocalendar(datetime.today())

##    my_birth=datetime(1992,1,1)
##    cacl_birth(my_birth)
##    print days_until_birthday(my_birth)
    # compute the day one person is twice as old as another
    b1 = datetime(2006, 12, 26)
    b2 = datetime(2003, 10, 11)
    print 'Double Day',
    print double_day(b1, b2)
