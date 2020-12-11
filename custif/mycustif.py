#!/usr/bin/env python3

"""
Author: NASnyder

This program tests if, elif, and else checks
"""

age = int(input("How old are you?"))       # ask for user age

def main():
    """main program"""
    if age < 10:
        print("You are younger than 10.")  # if input is less than 10, print

    elif age < 25:
        print("You are younger than 25.")  # if input is less than 25, print

    elif age < 50:
        print("You are younger that 50.")  # if input is less than 50, print

    else:
        print("You are 50 or older.")      # else, print


main()
