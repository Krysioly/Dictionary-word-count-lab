# put your code here.

import string

def find_word_count(input_file):
    file = open(input_file)
    words_dict = {}

    for line in file:
        line_words = line.split()
        # line_words = line.split(" ")
        for word in line_words:
            for c in word:
                if c in string.punctuation:
                    word= word.strip(c)
            words_dict[word] = words_dict.get(word, 0) + 1

    for word, count in words_dict.items():
        print("{} {}".format(word, count))

find_word_count("test.txt")

