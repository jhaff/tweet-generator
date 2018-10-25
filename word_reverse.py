#Reverses one word when run like so: python3 word_reverse.py example
import sys

input = sys.argv[1:] #take everything but the first param
word = input.pop()
print(word[::-1])
