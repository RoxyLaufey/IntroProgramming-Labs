# CMPT 120 - Lab #6
# Roxy Lai
# 25-10-18
###


def showIntro():
    print("\n")
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")


def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")


def numbers():
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("\nYou have entered something other than a NUMBER!")


def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ")
        cmd = cmd.lower().strip()
        if cmd == "add":
            num1, num2 = numbers()
            result = num1 + num2
        elif cmd == "sub":
            num1, num2 = numbers()
            result = num1 - num2
        elif cmd == "mult":
            num1, num2 = numbers()
            result = num1 * num2
        elif cmd == "div":
            num1, num2 = numbers()
            result = num1 // num2
        elif cmd == "power":
            num1, num2 = numbers()
            result = num1 ** num2
        elif cmd == "quit":
            break
        else:
            print("That command is not supported. Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'")
            continue

        print("The result is " + str(result) + ".\n")


def main():
    showIntro()
    doLoop()
    showOutro()


main()

