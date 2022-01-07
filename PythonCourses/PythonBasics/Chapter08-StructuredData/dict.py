#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    animals = {'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
               'giraffe': 'I am a giraffe!', 'dragon': 'rawr'}

    # add value
    animals["monkey"] = "haha"
    print_dict(animals)


def main2():
    animals = dict(kitten='meow', puppy='ruff!', lion='grrr',
                   giraffe='I am a giraffe!', dragon='rawr')
    print("Printing dictionary using constructor:")
    print_dict(animals)


def print_dict(o):
    for key, value in o.items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    main()
    main2()
