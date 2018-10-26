"""chooses however many random words from the unix dictionary as the user specifies"""

from sys import argv
from random import randint
# Lets you get a random line from a text file
from linecache import getline

def pick_random_words(words_amt):
    counter = 0
    words = ''
    total_words = 235885

    while counter < words_amt:
        #choose a random line of the file, therefore a random word
        words += getline("/usr/share/dict/words", randint(0, total_words))
        counter += 1
    return words

if __name__ == "__main__":
    words_num = int(argv[1])
    print(pick_random_words(words_num))
