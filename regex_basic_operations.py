#!/usr/bin/env python3.7

'''
#re Operations


re.search(pattern, text)
re.match(pattern, text)
re.finditer(pattern, text)
re.findall(pattern, text)

'''

import re

#print(re.findall('is','This is python and it is easy to learn'))
text='This is python and it is easy to learn'
my_pat='is'
print(re.findall(my_pat,text))
pat1='i[st]'
print(re.findall(pat1,text))


# Rules to create pattern

'''
a, x, 9  	- Ordinary characters that match themselves 
'''

text='x is greater than 9x'
#patt='a'
patt='x'
print(re.findall(patt,text))

'''
[abc]  		- match a or b or c
[a-z]		- match all a to z characters
'''
text='a very big cat'
#patt='[abc]'
patt='[a-t]'
print(re.findall(patt,text))


'''
[a-zA-Z0-9]		- Matches (a-z) or (A-Z) or (0-9)
'''
text="Learning Python3.7"
patt='[a-eL-Q2-7]'
print(re.findall(patt,text))

'''
\w Matches a-z, 0-9 and _
'''
#Match single character using \w
text="Learning @Python3.7 _ some __text-more text"
patt="\w"
print(re.findall(patt,text))
#Match two characters string using \w
patt1="\w\w"
print(re.findall(patt1,text))
#Match 3 character string using \w\w\w
patt2="\w\w\w"
print(re.findall(patt2,text))

'''
\W - Matches all characters which are not part of \w
'''
patt3="\W"
print(re.findall(patt3,text))

'''
\d
'''
text1="python2 and python3 and python37"
patt4="\d"
patt5="\w\w\w\d"
patt6="python\d\d"
print(re.findall(patt4,text1))
print(re.findall(patt5,text1))
print(re.findall(patt6,text1))


'''
. (dot) - Matches every single charater except newline \n
'''
text2="python2 and python3 and python3.7"
mypat="."
mypat1="..."  # matches 3 characters in sequence
mypat2="\."   # matches only dot
print(re.findall(mypat,text2))
print(re.findall(mypat1,text2))
print(re.findall(mypat2,text2))


## Extacting IP from string 

iptext="extracting IP from this string 100.200.102.200 43434009992353"
ippat1="\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"
print(re.findall(ippat1,iptext))



