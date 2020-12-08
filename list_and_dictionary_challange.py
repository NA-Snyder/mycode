#!usr/bin/env python3

dog_names = ["Jewel", "Molly", "Dude"] # create list of dog names
cat_names = ["Shadow", "Lana", "Jasmine"] # create list of cat names

dog_names.append(cat_names) # appends cat name list to dog name list

print(dog_names)
print(dog_names[0])
print(dog_names[3][1])

names = {"first_dog": dog_names[0], "second_cat": dog_names[3][1]} # create dictionary of names

print(names)
print(names["first_dog"])
print(names["second_cat"])
