#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = ''' 
This is a multi-line string. 
This is the second line.
'''
print('x is {}'.format(x))
print(type(x))

s = 'This is a string. '.upper()
print(s)


# 1:<4 means that there should be 4 spaces in total (can be exceeded though)
# Left align 9 by 4 spaces, and right align 8 by 3 spaces
t = 'seven "{1:<4}" "{0:>3}"'.format(8, 9)
print(t)

# Left align 9 by 4 spaces, and right align 8 by 3 spaces - filled by zeros
t = f'seven "{9:<04}" "{8:>03}"'
print(t)
