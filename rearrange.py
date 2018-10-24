import sys #access command line arguments
import random # for generating random numbers

if __name__ == '__main__':
    params= sys.argv[1:] # take a sublist starting from index 1 till the end
    random.shuffle(params)
    print(params)
