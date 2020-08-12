#!/usr/bin/env python3.7

'''
re.compile() is used to create pattern object, in case of if you want to perform multiple operations (e.g search(), match(), findall() , split()) on same pattern

operations on compiled pattern object are faster than using plane pattern
'''

import re

mytxt="this is python ; this is Python ; this is python2 ; this is python3"
mypat=r'\b[pP]ython[23]?\b'
pat_obj=re.compile(mypat)  # support flags= e.g flags=re.I
print(pat_obj)

print(pat_obj.search(mytxt))
print(pat_obj.findall(mytxt))
print(pat_obj.split(mytxt))

