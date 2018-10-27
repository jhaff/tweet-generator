"""Script that takes a .txt as a command line argument and counts every instance of every word.
Uses a tuple with the word and its count, inserted into a list of tuples.
"""

import sys

def histogram(words):
    word_list = []
    for word in words:
        if word not in word_list:
            # count() function in an inbuilt function
            # that returns the number of occurrences of a substring in the given string.
            word_list.append((word, words.count(word))); #add a tuple containing the word and its count to word_list
    return word_list

#opens a file once so the program needs not do it over and over
def open_and_split_file(filename):
    #open the file, read each line and split into an array of words based on spaces
    words = open(sys.argv[1], "r").read().split()
    return words

filename = sys.argv[1] #user specified file to read
words_to_analyze = open_and_split_file(filename)
print(histogram(words_to_analyze))
