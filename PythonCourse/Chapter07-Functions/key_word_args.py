#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Keyword Arguments like list arguments that are dictionaries instead of tuples


def main():
    kitten(Buffy='meow', Zilla='grr', Angel='rawr', Serhat='hooooo')


def main2():
    x = dict(Buffy='meow', Zilla='grr', Angel='rawr', Serhat='heeeeeeeeee')
    kitten(**x)


def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else:
        print('Meow.')


if __name__ == '__main__':
    main()
    main2()
