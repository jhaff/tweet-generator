"""
Randomly shuffles command line arguments
"""
import sys #access command line arguments
import random # for generating random numbers

def rearrange_words(words):
    shuffled_words = ""
    words_array = words #make a copy of input
    for i in range(len(words)):
        random_index = random.randrange(len(words_array)) #choose a random index within our words array
        shuffled_words += "{} ".format(words_array[random_index]) #add the selected word to the shuffled string
        del words_array[random_index]
    return shuffled_words

if __name__ == '__main__':
    params = sys.argv[1:] # take a sublist starting from index 1 till the end
    print(rearrange_words(params))
