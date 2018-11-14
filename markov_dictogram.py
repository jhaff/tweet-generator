from dictogram import Dictogram

class Markov_Dictogram(Dictogram):
    """This generates a markov chain given a word list.
    The chain consists of multiple dictionaries within a larger dictionary.
    For example, the Markov_Dictogram of one fish two fish red fish blue fish
    would look like :
    one {
        fish: 1
    }
    fish{
        two: 1
        red: 1
        blue: 1
    }
    two {
        fish: 1
    }
    red{
        fish: 1
    }
    blue{
        fish: 1
    }
    """

    def __init__(self,word_list=None):
        super(Markov_Dictogram,self).__init__

        if word_list is not None:
            #loop through the word list given to create a markov chain
            for i in range(len(word_list) - 1):
                self.add_count(word_list[i],word_list[i+1])

    def add_count(self,word,next_word):
        if word in self:
            #if the word already represents a key in the markov dictogram,
            if next_word in self[word]:
                #if the inner dictionary already has this word, increment its val
                self[word][next_word] += 1
            else:
                #if the inner dictionary lacks the word, insert it with val = 1
                self[word][next_word] = 1
        else:
            #if the word is not yet in the markov dictogram, add it with a
            #new dictionary to begin storing words that come after each Instance
            #of this word
            self[word] = {next_word:1}

        #for finding how often the second word comes after the first
    def frequency(first_word,second_word):
        if second_word in self[first_word]: #if the 1st ever comes after the 2nd,
            #return the value of the innermost dictionary representing how many
            #times the second word came after the first
            return self[first_word][second_word]
        else: #return 0 if the second word has never come after the first.
            return 0
