#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys


def main():
    try:
        # x = int('foo')
        x = 5/0
        # x = 5
    except ValueError as exception:
        print('I caught a ValueError! ' + str(exception))
    except ZeroDivisionError:
        print('Don\'t divide by zero!')
    except:
        print(f'Unknown error: {sys.exc_info()}')
    else:
        print('No exceptions occurred!')


if __name__ == '__main__':
    main()
