import string

f = open("2.txt", "r")
huge_string_of_death = f.read()


def find_letters(text):
    for letter in text:
        if string.ascii_lowercase.find(letter) != -1:
            print(letter, end="")


find_letters(huge_string_of_death)