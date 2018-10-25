"""
Randomly shuffles command line arguments
"""

import sys #access command line arguments
import random # for generating random numbers

def rearrange_words(words):
    for i in range(len(words)):
        random_index = random.randrange(len(words))
        print(words[random_index])
        del words[random_index]

if __name__ == '__main__':
    params = sys.argv[1:] # take a sublist starting from index 1 till the end
    rearrange_words(params)
