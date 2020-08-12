#!/usr/bin/env python3.7

import re

'''
search() operation 	- Looks into entire string and returns only first match; by default looks into multiple lines sting

match() operation	- Looks only in single line string and at 0 index Only; this is difference between search() and match()

'''

mytxt="learning python python2 python3 and in future python4"
mypat=r'\bpython[23]?\b'
#print(re.findall(mypat,mytxt))
#print(re.search(mypat,mytxt)) #will only finds first match i.e 'python'

match_obj=re.search(mypat,mytxt)

if match_obj: ## Error handling if no match found

    print("my matched stings are: ",match_obj.group())
    print("starting index of mymatch is : ",match_obj.start())
    print("End index of match is : ",match_obj.end()-1)
    print("Length of mathc is : ",match_obj.end()-match_obj.start()-1)
else: 
    print("No match found")

## Multiline example

mytxt1="""this is python
this is python2
this is python3"""
mypat1=r'\bpython[23]?\b'
match_obj=re.search(mypat1,mytxt1)
print("my matched stings is: ",match_obj.group())


## Use of match()
mytxt2="""python is easy   
this is python2
this is python3"""
mypat2=r'\bpython[23]?\b'
match_obj=re.match(mypat2,mytxt2)
print("my matched stings is: ",match_obj.group())
print("starting index of mymatch is : ",match_obj.start())

