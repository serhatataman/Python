#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    # r: read only mode (default)
    # w: write (overwrites) - creates file if it doesn't exist
    # a: append (doesn't overwrite)
    # r+: read and write (overwrites) - creates file if it doesn't exist
    # w+: write and read (overwrites) - creates file if it doesn't exist
    # a+: append and read
    # b: binary mode
    # t: text mode (default)
    # x: create file if it doesn't exist
    # +: read and write
    # U: universal newline mode
    # s: don't buffer output
    f = open('lines.txt', 'r')  # open file for reading
    for line in f:
        print(line.rstrip())


if __name__ == '__main__':
    main()
