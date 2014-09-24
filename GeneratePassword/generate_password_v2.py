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

def generate(password_length, at_least_one_letter, at_least_one_number, at_least_one_punctuation):
    """Generate a password by include enough random
    characters to meet the password length restriction.

    In addition, the user can specify that at least one
    of the each of the classes of character be used.
    """
    #
    # Any combination of characters is valid
    #
    valid_characters = ""
    if at_least_one_letter:
        valid_characters += letters
    if at_least_one_number:
        valid_characters += numbers
    if at_least_one_punctuation:
        valid_characters += punctuation

    #
    # Start with a blank password and then go round enough
    # times to make a password of the required length.
    #
    password = ""
    for i in range(password_length):
        #
        # Each time around, ensure that one of each of the selected
        # groups is chosen, and then just choose randomly from all
        # groups.
        #
        if at_least_one_letter:
            character = random.choice(letters)
            at_least_one_letter = False
        elif at_least_one_number:
            character = random.choice(numbers)
            at_least_one_number = False
        elif at_least_one_punctuation:
            character = random.choice(punctuation)
            at_least_one_punctuation = False
        else:
            character = random.choice(valid_characters)
        password += character

    #
    # Finally, shuffle the password so we don't always get a
    # letter at the beginning, with a number after and some
    # punctuation.
    #
    characters = list(password)
    random.shuffle(characters)
    password = "".join(characters)
    return password

if __name__ == '__main__':
    password_length = int(input("How many letters? "))
    at_least_one_letter = "Y" == (input("At least one letter [Y/n]? ").upper() or "Y")
    at_least_one_number = "Y" == (input("At least one number [Y/n]? ").upper() or "Y")
    at_least_one_punctuation = "Y" == (input("At least one punctuation [Y/n]? ").upper() or "Y")
    password = generate(password_length, at_least_one_letter, at_least_one_number, at_least_one_punctuation)
    print("Your password is: {}".format(password))
