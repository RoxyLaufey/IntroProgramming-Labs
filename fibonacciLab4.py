#  Introduction to programming
#  Date: 9/20/18
#  separate variables for the result, the previous Fibonacci number, and the Fibonacci
#  number before the previous one.
#  loop, count up to n and compute the next result, being sure
#  to update the previous and one-before-the-previous variables as you go.
# Fibonacci series:
# the sum of two elements defines the next


def main():
    n = int(input("Enter how many terms you want in this series: "))
    first = 1
    second = 1
    for i in range(n):
        print(first)
        temp = first
        first = second
        second = temp + second


main()
