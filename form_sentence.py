import sample

"""generates a sentence with use of the markov histogram"""
def generate_markov_sentence(word_histogram,markov_histogram,amount_of_words):
    word_list = [] #initialize empty word list
    if len(word_histogram) == 0: #if the histogrm is empty,
        raise Exception("No words given")

    word = sample.weighted_random_word(word_histogram) #generate the first word

    while len(word_list) is not amount_of_words: #do this until we have enough
        word_list.append(word) #add the word to the list
        #change the word to a sampled weighted word from the inner dictionary
        #in the markov histogram of that word
        word = sample.weighted_random_word(markov_histogram[word])
    return " ".join(word_list)

def generate_second_order_markov_sentence(markov_histogram,amount_of_words):
    """generates a sentence with use of the markov histogram"""
    """MUST pass in a SECOND order markov histogram."""
    word_list = [] #initialize empty word list
    if len(markov_histogram) == 0: #if the histogrm is empty,
        raise Exception("No words given")
    word = random.choice(list(markov_histogram)) #generate the first word
    while len(word_list) is not amount_of_words: #do this until we have enough
        word_list.append(word[1]) #add the word to the list(from the dictogram)
        #change the word to a sampled weighted word from the inner dictionary
        #in the second order markov histogram of that word
        word = (word[1],sample.weighted_random_word(markov_histogram[word]))
    word_list[0] = word_list[0].capitalize() #capitalize the first word for our sentence
    return " ".join(word_list) + "."
