#!/usr/bin/env python3.7

'''

## pass command line arguments to the script to test
## ./module-sys-command-arguments.py hello world 2 3 4
import sys

print(sys.argv)  # Returns command line arguments as list

'''

## e.g ./module-sys-command-arguments.py 'hello World' upper

import sys


if len(sys.argv) != 3:
   print("Usage:")
   print(f"{sys.argv[0]} <'string name'> <upper|lower|title>")
   sys.exit()

my_str=sys.argv[1]
my_action=sys.argv[2]

if my_action == "upper":
   print(sys.argv[1].upper())
elif my_action == "lower":
   print(sys.argv[1].lower())
elif my_action == "title":
   print(sys.argv[1].title())
else:
   print("Usage:") 
   print(f"{sys.argv[0]} <'string name'> <upper|lower|title>")


