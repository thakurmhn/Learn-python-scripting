#!/usr/bin/env python3.7


'''
^ 	- start of string or start of line in case of multiple line string
'''
import re

text="it is python and it is easy to learn"
pat='^i[ts]'
print(re.findall(pat,text))


'''
$  	- Matches end of the string
'''

text="it is python and it is easy to learn"
pat='learn$'
print(re.findall(pat,text))

'''
\b   	- matches empty string at the begining of the given string
 
'''
text="it is python andlearn it is learn easy to learn"
pat='\\blearn'	# two \\ as \b is backslash charater and need to escape
# OR write 'r' - raw sting
pat=r'\blearn'
print(re.findall(pat,text)) # not matching first occurrence of learn as there is no space before it

text="it is python andlearn it isilearn easy to learn"
pat=r'\blearn\b'  # matching only learn word 
print(re.findall(pat,text))  

'''
\B	- Empty string NOT at begining or end of the string, inverse to \b
'''

text="it is python andlearnit is learn easy to learn"
pat=r'\Blearn\B'  # finds 'learn' where no spaces at the start or at end of the word 'learn' i.e (andlearnit)
print(re.findall(pat,text))  


'''
{}	- {2}, 	- Exactly 2 times
{2,4}	- matchs 2, 3 or 4 times
{2,}	- 2 or more times
'''

text="pythonn aaaa "
pat=r'python{2}'
pat2=r'\ba{4}\b'  # matches 'a' four times; \b is word boundry
text1="pythonn aaaa pythonnnn"
pat3=r'python{2,4}'  # matches n' two, three or fourtimes
print(re.findall(pat,text))
print(re.findall(pat2,text))
print(re.findall(pat3,text1))


mytext="xaz xaaaaz sdfaaaaaaddda sdfdfaaaalll xaaazzz xaaaaaaaaz"
mypat=r'xa{2,}z'
print(re.findall(mypat,mytext))


'''
+	- matches character one or more times; same as {1,}
'''

mytext="xaz xaaaaz sdfaaaaaaddda sdfdfaaaalll xaaazzz xaaaaaaaaz"
mypat=r'xa+z'
print(re.findall(mypat,mytext))

'''
*	- matches character 0 or more times
'''
mytxt="xaz xaaaaz xaaazzz xz xaaaaaaaaz"
mypat1=r'xa*z'	# will match 'xz' also
print(re.findall(mypat1,mytxt))

'''
?	- matches character having occurrence one or none times
'''

mytxt1="xaz xaaaaz xaaazzz xz xaaaaaaaaz"
mypat2=r'xa?z'  # will match 'xaz' and xz
print(re.findall(mypat2,mytxt1))


'''
[]	- [23] matches 2 or 3
'''

mytxt="I have python, python2 and python3"
mypat=r'\bpython[23]?\b'
print(re.findall(mypat,mytxt))
