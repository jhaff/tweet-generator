import random
from dictogram import Dictogram
from split_text_file import tokenize_text

def generate_weights(word_list):
    weights = []
    words_seen = []
    #super DUPER innefficient but gets the job done :)
    for word in word_list:
        if word not in words_seen:
            word_count = word_list.count(word)
            weight = word_count/len(word_list) #weight is the word count/total words
            weights.append(weight)
            words_seen.append(word)

    weights_and_count = list(zip(words_seen, weights)) #list of tuples! (word/weight)
    return weights_and_count

def weighted_probablity(weighted_histogram, num_trials):
    # this list will hold all the generated words
    results = []
    # the number of times that we will run this function
    for _ in range(num_trials):
        # setting up a while loop so that we always return a value
        not_chosen = True
        while not_chosen:
            # randomly choose a list from our list of lists
            random_choice = random.choice(weighted_histogram)

            word, probability = random_choice
            # randomly generating a float between 0 and 1 inclusive
            random_number = random.uniform(0,1)
            # compare the probability with the random number
            if probability > random_number:
                # if probability is bigger then we get that word
                results.append(word)
                not_chosen = False
    # slow method, but it works
    return results

if __name__ in '__main__':
    word_list = tokenize_text("small_sample.txt")
    print("WEIGHTS")
    print(generate_weights(word_list))
    weighted_histogram = generate_weights(word_list)
    results_list = weighted_probablity(weighted_histogram, 1000)
    # using dictogram function
    results_histogram = Dictogram(results_list)
    print("RESULTS")
    print(results_histogram)
