# Author: Roxanne Lai
# CMPT 120L 113
# Introduction to programming
# Date: 10/18/18


def main():
    print("GAME FINISHED")
answer = "cat"
guess = "dog"
getOut = "quit"

while not guess == answer:
    print("PYTHON GUESSING GAME.")
    print("I am thinking of an animal...")
    guess = str(input("guess the name of the animal: "))
    userGuess = guess.lower().strip()
    if userGuess == getOut[0]:
        print("sorry this game is too hard for you!")
        break
    elif userGuess == answer:
        print("you guessed correctly, congrats!")
        feeling = str(input("do you like the animal? type yes or no: "))
        if feeling == "yes":
            print("I like cats too!")
            break
        else:
            print("You are so mean, cats are amazing!")
            break
    else:
        print("You did not guess the right animal, guess again")

main()
