# Author: Roxanne Lai
# CMPT 120L 113
# Introduction to programming
# Date: 9/6/18
#   A program that computes the real roots of a quadratic equation
#   Illustrates use of the math library
#   Note: This program crashes if the equation has no real roots, so coefficient "c" must be a negative number

import math  # Makes the math library available


def main():
    print("This program finds the real solutions to a quadratic")
    print()
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    discroot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discroot) / (2 * a)
    root2 = (-b - discroot) / (2 * a)
    print()
    print("The solutions are:", root1, root2)


main()