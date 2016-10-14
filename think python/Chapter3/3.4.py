def do_twice(f,name):
    f(name)
    f(name)

def do_four(f,name):
    f(name)
    f(name)

def print_twice(name):
    print name
    print name

if __name__=="__main__":
    do_twice(print_twice,'spam')
    do_four(print_twice,'spam')
