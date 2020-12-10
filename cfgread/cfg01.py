#!/usr/bin/env python3

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

######## EXPLORE READ ##########
## create file object in "r"ead mode
configfile = open(f"{dir_path}/vlanconfig.cfg", "r")

## display file to the screen - .read()
print(configfile.read())

## close file
configfile.close()

######## EXPLORE READLINES ##########
## re-create file object to explore new method
configfile = open(f"{dir_path}/vlanconfig.cfg", "r")

## make a list of file lines - .readlines()
configlist = configfile.readlines()
print(configlist)

## Iterate thrhough configlist
for x in configlist:
    print(x, end="")

## Always close your file
configfile.close()

