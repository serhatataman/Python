#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# CRUCIAL NOTE: Python does not have private variables. But underscore (_) indicates that the variable should be
# treated as private and should not be accessed directly.

class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    # This method serves as both getter and setter
    def type(self, t=None):
        if t:
            self._type = t
        return self._type

    def name(self, n=None):
        if n:
            self._name = n
        return self._name

    def sound(self, s=None):
        if s:
            self._sound = s
        return self._sound

    # This is like toString() method in Java
    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'


def main():
    a0 = Animal(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal(type='duck', name='donald', sound='quack')
    a0.sound('bark')
    print(a0)
    print(a1)


if __name__ == '__main__':
    main()
