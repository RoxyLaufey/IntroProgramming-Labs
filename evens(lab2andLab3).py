# Author: Roxanne Lai
# CMPT 120L 113
# Introduction to programming
# Date: 9/6/18
# A program that uses a for loop - printing all even integers between 2 and 20


def main():
    for i in range(2,21):
        if i % 2 == 0:
            print(i)
        else:
            print("something went wrong")


main()
