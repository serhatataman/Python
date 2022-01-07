#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


x = 'Hello, World.'
print(repr(x))  # repr() returns a string that can be evaluated to produce the original object - means representation

a = (1, 2, 3, 4, 5)
b = list(reversed(a))
c = sum(a)
d = max(a)
e = min(a)

print('original tuple: ' + str(a))
print('Reversed: ' + str(b))
print('Sum: ' + str(c))
print('Max: ' + str(d))
print('Min: ' + str(e))

print('\nZip them together: ')
f = (6, 7, 8, 9, 10)
g = zip(a, f)
for j, k in g:
    print(f'{j} - {k}')

print('\nEnumerator: ')
animals = ('cat', 'dog', 'monkey', 'tiger', 'lion')
for index, value in enumerate(animals):  # enumerate(animals) returns index and its value
    print(f'{index} - {value}')
