import os, sys
import random
import string

try:
    # Make Python2 work like Python3
    input = raw_input
except NameError:
    # On Python3; already using input
    pass

letters = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation

def generate(password_length):
    """Generate a password by include enough random
    characters to meet the password length restriction
    """
    #
    # Any combination of characters is valid
    #
    valid_characters = letters + numbers + punctuation

    #
    # Start with a blank password and then go round enough
    # times to make a password of the required length.
    #
    password = ""
    for i in range(password_length):
        #
        # Each time around, add a randomly-chosen character
        # random.choice picks one from a list
        #
        password += random.choice(valid_characters)

    return password

if __name__ == '__main__':
    password_length = int(input("How many letters? "))
    password = generate(password_length)
    print("Your password is: {}".format(password))
