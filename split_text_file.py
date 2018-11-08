# Module taking corpus text and converting it to tokens to be returned as a list

def split_text(text_file):
    ''' Takes raw text and will returns a split list of all the words in the text file '''
    try:
        with open(text_file, 'r') as file:
            return file.read().replace('\n', '').lower().split()
    except IOError:
        raise Exception('Could not open the file. Ensure it is a .txt and try again')

if __name__ == "__main__":
    print(split_text("small_sample.txt"))
