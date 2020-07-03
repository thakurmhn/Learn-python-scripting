#!/usr/bin/env python3.7

## Remove start/end spaces 

S1="  python  "
print(S1.strip())

S2=(S1.strip())
print(S2.strip('p'))
print(S2.strip('n'))

S3="python scripting is easy"
print(S3.strip('easy'))

print(S3.rstrip('easy'))
print(S3.lstrip('py'))


S4="python./u"
S4=S4.strip('./u')
print(S4)

x="pythonyy"
print(x.strip('y').strip('p'))

s="this is very big string"
print(s.split())


# Count number of occurrences of the string 

x="python is very good for scripting and is very popular and is easy"
print(x.count('is'))
print(x.count('p'))


# identify index of the character
print(x.index('v'))

print(x.index('v',11)) # again start counting for index at 11 to find next occurrence of 'v'
print(x.index('is'))


# use find() to identify index. It does not give error in absence of string 

print(x.find('p'))
print(x.find('p',1))
print(x.find('p',29))
print(x.find('p',47))
print(x.find('p',49)) # -1 is no further indexes found however index() produce error in this case

print(x.find('z'))





