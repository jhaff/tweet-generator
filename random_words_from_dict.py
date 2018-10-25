#chooses however many random words from the unix dictionary as the user specifies

from sys import argv
from random import randint
# Lets you get a random line from a text file
from linecache import getline

def pick_random_word(words_amt):
    counter = 0
    word = ''
    while counter < words_amt:
        #choose a random line of the file, therefore a random word
        word += getline("/usr/share/dict/words", randint(0, 235885))
        counter += 1
    print(word)

def main():
    number = int(input("How many words do you want? Enter an integer."))
    print(pick_random_word(number))

if __name__ == "__main__":
    main()
