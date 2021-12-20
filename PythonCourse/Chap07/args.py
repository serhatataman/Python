#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    print("Main:")
    kitten('meow', 'grrr', 'purr', 5, 7.12, False)


def main2():
    print("Main2:")
    x = ('meow', 'grrr', 'purr', 5, 7.12, False)
    kitten(*x)


def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print('Meow.')


if __name__ == '__main__':
    main()
    main2()
