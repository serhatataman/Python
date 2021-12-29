#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42 * 747 * 1000
y = 931
print('The number is {:,}'.format(x))  # Put commas in the number as a thousand separator
print('Decimals: The number is {:.3f}'.format(x))  # Use only 3 decimals after the decimal point
print('Binary number is {:b}'.format(x))  # print out the number in binary
print('Octal number is {:o}'.format(x))  # print out the number in octal
print('Hexadecimal number is {:x}'.format(x))  # print out the number in hexadecimal
print('Formatted numbers are {0:<5} and {1:>05}'.format(x, y))  # Left align the first number and right align the second number with leading zeros


# Casefold works with unicode letters too. \xdf is a representation of capital german letter B
print('Casefold: Hello, world! \xdf'.casefold())
# Whereas lower does not work with unicode letters.
print('Lower: Hello, world! \xdf'.lower())

print('Swapcase: Hello, World.'.swapcase())
print('Title: Hello, World.'.title())
print('Upper: Hello, World.'.upper())
print('Format: Hello, World. {}'.format(42*7))

print('''
    Hello,
    World.
''')


# Inherit from build-in str class
class MyString(str):
    def __str__(self):
        return self[::-1]


s = MyString('Hellow, World.')
print(s)


