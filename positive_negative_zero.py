#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Sept 2021
# This program will tell you if your number is positive, negative, or zero


def main():
    # this function tells you if your number is positive, negative, or zero

    # input
    user_number = int(input("Enter an integer: "))

    # process
    if user_number > 0:
        print("{0} is a positive number.".format(user_number))
    elif user_number < 0:
        print("{0} is a negative number.".format(user_number))
    else:
        print("{0} is just zero!".format(user_number))

    # output
    print("\nDone.")


if __name__ == "__main__":
    main()
