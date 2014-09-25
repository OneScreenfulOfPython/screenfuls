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
    word_matcher = re.compile(r"\w{3,}")
    with open(filepath) as f:
        return set(w.group() for w in word_matcher.finditer(f.read()))

def generate(password_length):
    """Generate a password by include enough random
    characters to meet the password length restriction
    """
    return password

if __name__ == '__main__':
    password_length = int(input("How many letters? "))
    password = generate(password_length)
    print("Your password is: {}".format(password))
