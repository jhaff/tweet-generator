import random
import re

#initialize empty dictionary to hold the histogram
histogram_dictionary = {}

#Takes text and returns a histogram(dictionary) of word frequency that shows word frequency
def create_histogram(text):
    for word in text: #loop over each word in the input
        if word in histogram_dictionary:
            #increment counter for each word already in dict
            histogram_dictionary[word] += 1
        else:
            #add new place for each word not already in dict
            histogram_dictionary[word] = 1

    return histogram_dictionary


def random_word(histogram_dictionary):
    """Generates a random, weighted word from the histogram"""
    #Creates a running total value
    total_word_count = 0
    #Gets a random number between 0 and the total sum of all frequencies
    sum_dictionary = sum(histogram_dictionary.values())

    # Either [1,  sum] or [0, sum - 1] otherwise it repeats inappropraitely
    random_word_index = random.randint(0, sum_dictionary - 1)
    # ".items()" allows the dictionary to be iterated over
    for key, value in histogram_dictionary.items():
        total_word_count += value
        if total_word_count > random_word_index:
            return key
        else:
            continue

def dictionary_test(histogram_dictionary):
    test_dictionary = {}
    for _ in range(0, 10000):
        selected_word = random_word(histogram_dictionary)
        if selected_word in test_dictionary:
            test_dictionary[selected_word] += 1
        else:
            test_dictionary[selected_word] = 1
    return test_dictionary

def file_open():
    '''Opens and returns the file to be read for words'''
    with open('small_sample.txt', 'r') as text:
        # text_string = text.read().replace('\n', '').lower().split() #Not sure if .replace is necessary due to the regex
        text_string = text.read().lower()
        match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_string)
    return match_pattern

if __name__ == "__main__":
    #create neccessary variables to pass in
    text = file_open()
    histogram = create_histogram(text)

    #demonstrate all functionality
    print("histogram:")
    print(histogram)
    print("100 of random_word(histogram):")
    for _ in range(0,100):
        print(random_word(histogram))
    print("dictionary_test(histogram):")
    print(dictionary_test(histogram))
