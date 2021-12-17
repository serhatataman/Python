#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# A list is a sequence of mutable objects
x = [1, 2, 3, 4, 5]
x[2] = 'two'
print("List Mutable")
for i in x:
    print('i is {}'.format(i))


# A list is a sequence of mutable objects
a = list(range(5, 10))
a[3] = 357357357
print("Range mutable")
for i in a:
    print('i is {}'.format(i))


# End at 50 but step by 5
a = range(5, 50, 5)
print("Range Immutable")
for i in a:
    print('i is {}'.format(i))


print("Tuple Immutable")
# A tuple is a sequence of immutable objects
tuple_object = (1, 2, 3, 4, 5)
for i in tuple_object:
    print('i is {}'.format(i))


# A dictionary is a sequence of mutable objects
print("Dictionary Mutable")
d = {'one': 1, 'two': 2, 'three': 3}
d['three'] = 79
for k, v in d.items():
    print('k is {} and v is {}'.format(k, v))