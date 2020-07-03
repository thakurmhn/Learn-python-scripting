#!/usr/bin/env python3.7

## wiht os.system() you can execute os commands

import os

print(os.system("pwd"))
#print(os.system("ls"))

## you can see '0' at the end of each command output, which is retrun code
## to supress printing of zero do following

returncode=(os.system("ls"))
#print(f"command returncode is {retruncode}")

if  returncode == 0:
    print("command executed successfully")
else:
    print("Error executing command")

