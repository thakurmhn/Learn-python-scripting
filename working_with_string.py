#!/usr/bin/env python3.7

'''
my_name=""
my_lastname=" "

print(f'{bool(my_name)}')  ## bool of any empty variable is always False
print(f'{bool(my_lastname)}')  ## bool of non empty variable is always True
'''
'''
# Access string based  on Index values

fav_scripting="python scripting"
print(f"{fav_scripting[-1]}")
print(fav_scripting[0:5])
print(fav_scripting[-16:-6])


# Change or delete string
# You can not change/delete part of string but can replace entire string

fav_scripting="python"
print(fav_scripting)
del fav_scripting

print(fav_scripting)

'''
'''
# Find lenghth of string
fav_scripting="python scripting"
print(f"length of string is {len(fav_scripting)}")

#Concat
S1="python"
S2="Scripting"
print(S1+" "+S2+" "+"Tutorial")


print(f"{S1.lower()}")
print(f"{S2.upper()}")

'''
'''
# Print list of String Operations
S1="somestring"
print(dir(S1))
'''

S2="Mohan Thakur"
print(S2.swapcase())

S1="MOHAN THAKUR"
print(S1.title())

S3="PythoN ScriPTing tuTOrial"
print(S3.casefold())












