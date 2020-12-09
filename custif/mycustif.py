#!/usr/bin/env python3

# ask user age
age = int(input("How old are you?"))

# ouput based on user age
if age < 10:
    print("You are younger than 10.")

elif age < 25:
    print("You are younger than 25.")

elif age < 50:
    print("You are younger that 50.")

else:
    print("You are 50 or older.")

print("Exiting script")



