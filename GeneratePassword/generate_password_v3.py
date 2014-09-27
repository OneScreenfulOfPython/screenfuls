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
        #
        # re.findall returns a list of all instances matching a pattern
        # The pattern \w{3,} matches a word at least three letters long
        # f.read() reads the entire contents of a file into a string
        # set() returns a unique set of the values in an iterator
        #
        # So we have:
        #   A unique set of
        #     All words at least three letters long within
        #       The contents of the file f
        #
        return set(re.findall(r"\w{3,}", f.read()))

def generate(filename, password_length, number_of_words):
    """Generate a password consisting of words from a text, at least
    as long as password_length.
    """
    words = get_words_from_file(filename)
    #
    # We need enough letters to produce a word at least as long as
    # password length. We know how many words to use, so we do some
    # simple division-and-remainder maths to get the number of letters
    # long which they must be.
    #
    quotient, remainder = divmod(password_length, number_of_words)
    word_length = quotient + (1 if remainder else 0)
    #
    # Copy all words of the right length into another list
    # and shuffle it to avoid generating the same password several
    # times.
    #
    # This is a "list comprehension". It's equivalent to:
    # suitable_words = []
    # for w in words:
    #   if length(w) == word_length:
    #     suitable_words.append(w)
    #
    suitable_words = [w for w in words if len(w) == word_length]
    random.shuffle(suitable_words)
    #
    # Then return the right number of words, each starting with a
    # capital letter, joined together.
    #
    # list[:number] gives the first number of words
    # word.title() gives a version of the word with an initial capital
    # "".join(... list of words ...) returns all the words joined up
    #
    return "".join(w.title() for w in suitable_words[:number_of_words])

if __name__ == '__main__':
    filename = input("Filename: ")
    password_length = int(input("How many letters? "))
    number_of_words = int(input("How many words? "))
    password = generate(filename, password_length, number_of_words)
    print("Your password is: {}".format(password))
