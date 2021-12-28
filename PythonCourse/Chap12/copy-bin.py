#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('berlin.jpg', 'rb')  # rb = read binary
    outfile = open('berlin-copy.jpg', 'wb')  # wb = write binary
    while True:
        buf = infile.read(10240)  # Use 10kB as size of the buffer
        if buf:  # if there is data in the buffer
            outfile.write(buf)
            print('.', end='', flush=True)
        else:
            break

    outfile.close()
    print('\ndone.')


if __name__ == '__main__':
    main()
