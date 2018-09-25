# Author: Roxanne Lai
# CMPT 120L 113
# Introduction to programming
# Date: 9/21/18


def happy():
    print("Happy birthday to you! ")


happy()


def sing(person):
    happy()
    happy()
    print("Happy birthday, dear", person + ".")
    happy()


def main():
    sing("Fred")
    print()
    sing("Lucy")
    print()
    sing("Elmer")


main()