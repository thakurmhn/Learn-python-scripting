#!/usr/bin/env python3.6

import argparse

# Build parser object

parser=argparse.ArgumentParser(description="Read a file in reverse")

# Add Arguments

parser.add_argument('filename', help='the file to read')   ## This is positional argument where need to supply filename
parser.add_argument('--limit', '-l', type=int, help='Number of lines to read') ## This is optional argument
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')
parser.add_argument('--foo', '-f', action='store_true')
parser.add_argument('--bar', action='store_false')
parser.add_argument('--num', nargs=2)  # --num 3 4 ; accecept two arguments by default each option accept one argument
parser.add_argument('--num2', nargs='?', default=10) # accepts one argument
parser.add_argument('--num3', nargs='+') # --num3 2 3 4 5 6 ; all command-line args present are gathered into a list
#parser.add_argument('--foo', required=True)


args=parser.parse_args()
#print(args)


# Parse the Argument

with open(args.filename) as f:
    lines=f.readlines()
    lines.reverse()

    if args.limit:
        lines=lines[:args.limit]  # slice with --limit argument value

    for line in lines:
        print(line.strip()[::-1])

print("Value of --foo is:", args.foo)
print("Value of --bar is:", args.bar)
print("Value of limit is:", args.limit)
print("Value of num is:", args.num)
print("Value of num2 is:", args.num2)
print("Value of num3 is:", args.num3)
    



# Read the file, revers the content and printa




