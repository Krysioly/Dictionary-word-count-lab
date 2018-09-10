# put your code here.

import string
import sys
import collections

def find_word_count(input_file):
    """Inputs file and counts number of times each word appears

    Removes punctuation and capitalization

    """
    # file = open(input_file)
    # words_dict = {}

    # for line in file:
    #     line_words = line.split()
    #     # line_words = line.split(" ")
    #     for word in line_words:
    #         word = word.lower()
    #         for c in word:
    #             if c in string.punctuation:
    #                 word= word.strip(c)
    #         words_dict[word] = words_dict.get(word, 0) + 1

    # for word, count in words_dict.items():
    #     print("{} {}".format(word, count))

    file_string = open(input_file).read()
    text = file_string.lower()

    # This is not working!!!!
    for c in text:
        if c in string.punctuation:
            text=text.strip(c)

    words = text.split()

    for word, count in collections.Counter(words).items():
        print("{} {}".format(word, count))


find_word_count(sys.argv[1])

