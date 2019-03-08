"""Script that takes a .txt as a command line argument and counts every instance of every word.
Uses a list of lists.

Script unfinished. Bug where words are repeated in output persists.
"""

import sys

def histogram(words):
    words_with_their_counters_list = []
    for word in words:
        if word not in words_with_their_counters_list: #if we see a new word,
            #add a new array to the word list initialized with the new word its counter space as 1
            words_with_their_counters_list.append([word, 1])
        else: #if this is a word we've seen before...
            for item in words_with_their_counters_list: #loop through our list of lists
                if item[0] == word: #if the first item in each array within the wordlist array matches the word in the outer loop
                    item[1] += 1 #increment the word counter in the second spot of the inner array
    return words_with_their_counters_list

#opens a file once so the program needs not do it over and over
def open_and_split_file(filename):
    #open the file, read each line and split into an array of words based on spaces
    words = open(sys.argv[1], "r").read().split()
    return words

# filename = sys.argv[1] #user specified file to read
# words_to_analyze = open_and_split_file(filename)
# print(histogram(words_to_analyze))
