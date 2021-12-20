#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    # first value is the beginning, second is the end (non-inclusive) and the third is the step
    print(game[1:4:2])

    lizard_index = game.index('Lizard')
    print("index of Lizard is " + str(lizard_index))

    game.insert(0, 'Cheetah')
    game.remove("Paper")

    # game.pop() removes the last item in the list. It also returns the value that was removed
    removed_item = game.pop()
    print("Removed item is " + removed_item)

    print(", ".join(game))
    print_list(game)


def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()


if __name__ == '__main__': main()
