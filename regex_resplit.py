#!/usr/bin/env python3.7

## Working with split, substitue and subn

import re

#print(help(re.split))

mytxt="we are leaning python and python2 is old version  and Python3 is new version"
mypat=r'\bpython[23]?\b'
print(re.split(mypat,mytxt))  ## spliting at matched pattern i.e python, python2 python3
print(re.split(mypat,mytxt,flags=re.I))  ## Ignore cases 
print(re.split(mypat,mytxt,maxsplit=1,flags=re.I)) ## split only at first match

# sustitue - find and replace in place of pattern

print(re.sub(mypat,'java',mytxt,count=2,flags=re.I)) # count=2 replaces only two patterns


print(re.subn(mypat,'java',mytxt,flags=re.I)) ## shows number of places pattern is replaced


