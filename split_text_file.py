# Module for tokenizing + cleaning corpus text to be returned as a list
import re
import string

def tokenize_text(text_file):
    ''' Takes in raw text from a text file and will return a split()(list)
    of all the words in the text file '''
    try:
        with open(text_file, 'r') as myfile:
            # text_without_punctuation = myfile.read().translate(string.punctuation)
            remove_periods = re.sub('(\s\.){4,}', ' ', myfile.read())

            #remove any character that is not in a-z, A-Z whitespace.
            #Also remove end-of-line statements
            cleaned_first_sweep = re.sub('[^a-zA-Z\s]*$','',remove_periods)

            #allow the following
            white_list = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')

            #one more clean so that the above are the only characters we have
            cleaned_second_sweep = ''.join(filter(white_list.__contains__,cleaned_first_sweep))
            return cleaned_second_sweep.lower().split() #array of all words to lowercase
    except IOError:
        raise Exception('Could not open file. Ensure it is a .txt')

if __name__ == "__main__":
    print(split_text("small_sample.txt"))
