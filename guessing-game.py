# Author: Roxanne Lai
# CMPT 120L 113
# Introduction to programming
# Date: 10/18/18


def main():
    print("GAME FINISHED")
answer = "cat"
guess = "dog"


while not guess == answer:
    print("PYTHON GUESSING GAME.")
    print("I am thinking of an animal...")
    guess = str(input("guess the name of the animal: "))
    userGuess = guess.lower().strip()
    if userGuess == answer:
        print("you guessed correctly, you win!")
        break
    else:
        print("You did not guess the right animal, guess again")

main()
