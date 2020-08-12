#!/usr/bin/env python3.7

import re

'''
re.I or re.IGNORECASE	- makes regex case insensitive
re.L or re.LOCALE	- the behaviour of some special sequences like \w \W \b \s \S will be made dependent on current Locale i.e 
			User's language, country etc

re.M	or re.MULTILINE	- ^ and $ will match at begining and end of each line and not just the begining and end of the string

re.S	or re.DOTALL	- The "." will match every character plus newline

re.U	or re.UNICODE	- Makes \w,\W,\b,\B,\d,\D,\s,\S dependent on unicode character properties

re.X	or re.VEEBOSE	- Allowing verbose regex, i.e whitespaces are ignored
'''

mytxt="This is THIS and THIS is that this"
mypat=r'this'
print(re.findall(mypat,mytxt,re.I))


mytext="""this is first line
some more lines
That is first line
This is third line
this is fifth line
some more lines again
THis is some more text"""
mypatt=r'^this'
print(re.findall(mypatt,mytext,re.M)) ## Finds all lines begining with 'this'
print(re.findall(mypatt,mytext,re.M|re.I))	# two flags together separated with |
