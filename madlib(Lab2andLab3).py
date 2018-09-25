# Author: Roxanne Lai
# CMPT 120L 113
# Introduction to programming
# Date: 9/6/18
# A program that incorporates input and output statements, variable assignment, and string concatenation.


def makeAndPrintSentence():
    print("Once upon a time there was a", adjective, noun, ". It was", verb, "to get to the", place, "for a party. In the end the", noun, "made it on time!")


def promptForWords():
    global adjective, noun, verb, place
    adjective = input("Adjective: ")
    noun = input("Noun: ")
    verb = input("Verb: ")
    place = input("Place: ")


def main():
    print("Mad Libs")
    print("please enter a word for each part of speech")
    promptForWords()
    makeAndPrintSentence()


main()
