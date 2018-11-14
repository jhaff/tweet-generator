import random
import generate_histogram
#module to select one word based on commonness(frequency) in the given histogram

def weighted_random_word(histogram_dict):
    ''' Takes a histogram and returns a random weighted word '''
    # Raise an exception if we are given an empty histogram
    if len(histogram_dict) == 0:
        raise Exception("You can't sample from an empty histogram")
    #Creates a running total value
    total_word_count = 0
    #Gets a random number between 0 and the total sum of all frequencies
    sum_dictionary = sum(histogram_dict.values())

    # Either [1,  sum] or [0, sum - 1] otherwise it repeats inappropraitely
    random_word_index = random.randint(0, sum_dictionary - 1)
    # ".items()" allows the dictionary to be iterated over
    for key, value in histogram_dict.items():
        total_word_count += value
        if total_word_count > random_word_index:
            return key
        else:
            continue

def weighted_random_test():
    ''' Tests to make sure that the weighted random sampling is correct '''
    histogram = word_count.create_histogram('small_sample.txt')
    for _ in range(0,1000): #do the following 1000 times
        result_dict = {} #init empty dict to store results
        chosen_word = weighted_random_word(histogram)
        print(word_selected)
        if word_selected in result_dict:
            result_dict[chosen_word] += 1
        else:
            result_dict[chosen_word] = 1
    print(result_dict)
    return result_dict

if __name__ == "__main__":
    print(weighted_random_word(word_count.create_histogram('small_sample.txt')))
    weighted_random_test()
