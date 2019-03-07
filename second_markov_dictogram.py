from dictogram import Dictogram
class Second_Markov_Dictogram(dict):

    def __init__(self,word_list=None):
        super(Second_Markov_Dictogram,self).__init__
        if word_list is not None:
            length = len(word_list)-2 # -2 because now we look at two words at a time

            #loop through the word list given to create a markov chain
            for i in range(0, length):
                #passes in a tuple containing the current word, 2nd word & 3rd.
                self.add_count((word_list[i],word_list[i+1]),word_list[i+2])

    def add_count(self,word_tuple,next_word):
        if word_tuple in self: #if the pair already represents a key in the markov dictogram,
            if next_word in self[word_tuple]:
                #if this word pairing has the next word accounted for already,
                self[word_tuple][next_word] += 1 #increment existing value
            else:
                self[word_tuple][next_word] = 1 #create a new entry
        else:
            #if we have not seen these two words together yet,
            #create a histogram for them and add the next word as the first entry
            self[word_tuple] = {next_word:1}

    # def frequency(self,first_word,second_word):
    #     if second_word in self[first_word]:
    #         return self[first_word][second_word]
    #     else:
    #         return 0
