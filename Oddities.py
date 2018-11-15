def main():
    # read the input (first line) to know how many test cases
    n = int(input()) # no prompt text because Kattis doesn't want it in the output
    # loop that manny times to...
    for i in range(n):
        # read the next line of input
        x = int(input())
        # determine whether the number is odd or even
        if x % 2 == 0: # it's even
        # print an appropriate message
            print(x, "is even")
        else:
            print(x, "is odd")


main()