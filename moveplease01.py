#!/usr/bin/env python3

# import utilities
import shutil
import os

# allow program to run in any directory
os.chdir('/home/student/mycode/')

# move file to new location
shutil.move('raynor.obj', 'ceph_storage/')

# ask for user input
xname = input('What is the new name for kerrigan.obj? ')

# remane file with name from above input
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
