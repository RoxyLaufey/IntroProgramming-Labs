# Author: Roxanne Lai
# CMPT 120L 113
# Introduction to programming
# Date: 9/6/18
# A program that incorporates input and output statements, variable assignment, and string concatenation.


def story():
    adjective = input("Adjective: ")
    noun = input("Noun: ")
    verb = input("Verb: ")
    place = input("Place: ")
    print("Once there was a " + adjective + " " + noun + ". This " + noun + " was " + verb + " " + place + ". Luckily, the " + noun + " got there on time. Hurray!")


def main():
    print("Mad Libs")
    print("Please enter a word for each part of speech")
    story()


main()
