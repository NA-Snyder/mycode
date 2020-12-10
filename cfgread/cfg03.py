#!/usr/bin/env python3

loadfile = input("What file do you want to load?\n")
## create file object in "r"ead mode
with open(loadfile, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    filelines = 0
    configlist = configfile.readlines()
    for line in configlist:
        filelines += 1
    
## file was just auto closed (no more indenting)

## display list with no "\n"
print(configlist)
print(f"The number of lines in the file is: {filelines}")
