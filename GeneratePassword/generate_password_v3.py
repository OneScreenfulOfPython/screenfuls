import os, sys
import random
import re

try:
    # Make Python2 work like Python3
    input = raw_input
except NameError:
    # On Python3; already using input
    pass

def get_words_from_file(filepath):
    """Return the set of all words at least three letters
    long from within a named file.
    """
    with open(filepath) as f:
        return set(w.group() for w in re.finditer(r"\w{3,}", f.read()))

def generate(filename, password_length, number_of_words):
    """Generate a password consisting of words from a text, at least
    as long as password_length.
    """
    words = get_words_from_file(filename)
    word_length = (password_length + 1) // number_of_words
    suitable_words = list(w for w in words if len(w) == word_length)
    random.shuffle(suitable_words)
    return "".join(w.title() for w in suitable_words[:number_of_words])

if __name__ == '__main__':
    filename = input("Filename: ")
    password_length = int(input("How many letters? "))
    number_of_words = int(input("How many words? "))
    password = generate(filename, password_length, number_of_words)
    print("Your password is: {}".format(password))
