# Author: Roxanne Lai
# CMPT 120L 113
# Introduction to programming
# Date: 9/6/18
#  A program to calculate the value of some change in dollars


def main():
    print("Change Counter")
    print()
    print("please enter the count of each coin type.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("pennies: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    print()
    print("The total value of your change is", total)


main()