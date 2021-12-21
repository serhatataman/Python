#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a)
    print_set(b)
    print('Sorted order: \n')
    print_set(sorted(a))
    print_set(sorted(b))
    print("\nMembers are in set a but not in b:")
    print_set(a - b)
    print("\nMembers are in both set a and b or both:")
    print_set(a | b)
    print("\nMembers are in both set but not in a or b:")
    print_set(a ^ b)
    print("\nMembers are in only both:")
    print_set(a & b)


def print_set(o):
    print('{', end='')
    for x in o:
        print(x, end='')
    print('}')


if __name__ == '__main__':
    main()
