"""This script implements the Fisher Yates shuffle. It shuffles command line arguments in place.
It modifies the input list itself rather than creating a new, shuffled list.
"""

import random
import sys


def fisher_yates_shuffle(input_list):
    list_items_to_shuffle = len(input_list)
    counter = 1
    while list_items_to_shuffle > 0:
        rand_int = random.randint(0, list_items_to_shuffle-1)
        #Swap the randomly selected item with the nth to last item represented by (-counter)
        input_list[rand_int], input_list[-counter] = input_list[-counter], input_list[rand_int]
        counter += 1
        list_items_to_shuffle -= 1
    return input_list


if __name__ == '__main__':
    args = list(sys.argv[1:])
    print(fisher_yates_shuffle(args))
