# Author: Roxanne Lai
# CMPT 120L 113
# Introduction to programming
# Date: 9/6/18
# Mars Rover Program
# A program that calculates how long it takes for a photo from the Curiosity rover to NASA.
# Light travels at 186,000 MPH
# Distance is 34 million miles
# Time = Distance/Speed - Time = 34,000,000 mph / 186,000 mps (669600000 mph)


def main():
    time = 34000000 / 669600000
    print("The time to get from Curiosity to NASA is", time, "hours.")


main()