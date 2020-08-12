#!/usr/bin/env python3.7

import re

mytxt="I have python and python2 and python3"
mypat=r'\bpython[23]?\b'
print(re.findall(mypat,mytxt))

print(re.finditer(mypat,mytxt)) ## finditer() alway produce object whether match found or not found

my_obj=re.finditer(mypat,mytxt)

for each_obj in my_obj:
    #print(each_obj)
    #print(each_obj.group())
    print(f"Found match is : {each_obj.group()}\n Index Number of each match is : {each_obj.start()}")
