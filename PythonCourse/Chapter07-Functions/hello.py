#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def f1():
    print('This is f1()')


x = f1
x()


def f2(f):
    def f3():
        print('This is before the function call')
        f()
        print('This is after the function call')
    return f3


# f4 is being wrapped by f2. @f2 is a decorator. @f2(f4) is a wrapper. @f2 takes f4() and passes it to f2.
@f2
def f4():
    print('This is f4()')


f4()