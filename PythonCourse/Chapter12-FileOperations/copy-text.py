#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('lines.txt', 'rt')  # open file for reading text. rt is default, so we don't need to specify
    outfile = open('lines-copy.txt', 'wt')
    for line in infile:
        print(line.rstrip(), file=outfile)  # print line, stripping whitespace, to outfile
        # outfile.writelines(line)  # write line to outfile
        print('.', end='', flush=True)

    outfile.close()  # close outfile. This is important, otherwise the file will be locked.
    infile.close()  # close infile
    print('\ndone.')


if __name__ == '__main__':
    main()
