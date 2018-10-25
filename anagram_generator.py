# import sys
# Found on stack overflow but unsure how it aims to work, tried modifying for python3 and my needs but failed.
# def generate_anagrams(word):
#     if len(word) < 2:
#         yield word
#
#     else:
#         for i, letter in enumerate(word):
#             if not letter in word[:i]:
#                 for k in generate_anagrams(word[:i] + word[i+1:]):
#                     yield k+letter
#
# if __name__ == "__main__":
#     input = sys.argv[1:] #take everything but the first param
#     for i in generate_anagrams(input):
#         print i
