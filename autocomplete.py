"""This script returns a list suggested autocompletions for letters placed into
the command line arguments by iterating through the unix words list searching for words
that satisfy the regex pattern.
"""

import sys
import re #python Regular Expressions, or regex

#defined in its own function so that python only has to load in the whole list once
def read_sys_dict():
    #Open the words from the unix dictionary
    f = open('/usr/share/dict/words', 'r')

    #create array of words by replacing each new line in the dict with a space
    system_word_list = f.read().replace('\n', ' ').split() #now split using that space

    #When you’re done with a file, call f.close() to close it and free up any system
    #resources taken up by the open file. After calling f.close(), attempts to use the file object will automatically fail.
    f.close()

    return system_word_list

#Autocomplete the input word.
def autocomplete(word_start):
    word_list = read_sys_dict()
    regex_pattern = '^' + word_start #create the regex_pattern by appending a ^ to the user's input

    #Compile a regular expression pattern into a regular expression object,
    #which can be used for matching using its match(), search() and more methods.
    r = re.compile(regex_pattern)

    # filter creates a list of elements for which a function returns true
    matching_words = filter(r.match, word_list)

    return list(matching_words)

if __name__ == '__main__':
    input = sys.argv[1]
    autocomplete_suggestions = autocomplete(input)
    print(autocomplete_suggestions)
