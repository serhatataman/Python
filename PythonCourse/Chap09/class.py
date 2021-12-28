#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# The 'self' variable is a reference to the current instance of the class.
# In this case it is a reference to donald instance.

class Duck:
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'

    # the first parameter of the method is always self
    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)


def main():
    donald = Duck()
    donald.quack()
    donald.move()


if __name__ == '__main__':
    main()
