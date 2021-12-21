#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    seq = range(11)
    print_list(seq)

    # Print each element of the seq multiplied by 2
    seq2 = [x * 2 for x in seq]
    print("\nEach element multiplied by 2:")
    print_list(seq2)

    # Print each element of the seq which cannot be divided by 3
    seq2 = [x for x in seq if x % 3 != 0]
    print("\nEach element that cannot be divided by 3:")
    print(seq2)


def print_list(o):
    for x in o:
        print(x, end=' ')
    print()


if __name__ == '__main__':
    main()
