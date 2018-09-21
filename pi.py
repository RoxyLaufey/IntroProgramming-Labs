#  Author = Roxanne Lai
#  CMPT 120L 113
#  Introduction to programming
#  Date: 9/6/18
# Write a program that approximates the value of pi by summing the terms of this series:
# 4/1 – 4/3 + 4/5 – 4/7 + 4/9 – 4/11 + …
# The program should prompt the use for n,the number of terms to sum, and then output the sum
# of the first n terms of this series. Have your program subtract the approximation from the value
# of math.pi to see how accurate it is.
# Variables: one for the result, one for the next
# term to be added, and one to keep track of the sign. If you’re clever, you might notice that you can
# use the step parameter for your loop range to make it simpler to track the denominator of each term.


import math


def main():
    # pi = 4/1 – 4/3 + 4/5 – 4/7 + 4/9 – 4/11 + …
    Sum = 0 # set the sum = to 0
    n = eval(input("Enter how many terms you want to sum: "))
    denom = 1
    sign = 1 # the sign of the first term is positive, so sign = positive one
    for i in range(n):
        Sum = Sum + 4*sign/denom
# print(i,sign*denom,sum)
        denom = denom + 2
        sign = -sign

    print("Pi is approximately: ", Sum, "Pi is", math.pi)


main()



