import sample
import split_text_file

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
