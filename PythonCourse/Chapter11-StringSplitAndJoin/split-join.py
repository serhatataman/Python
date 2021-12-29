#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = '''This is a long             string with
 
 a bunch of           words in it.'''
print(s)

print('\nThe string split to array: ' + str(s.split()))

l = s.split()
s2 = '--'.join(l)
print(f'\nJoin the array to a string: {s2}')

print('\nSplit on letter i : ' + str(s.split('i')))
