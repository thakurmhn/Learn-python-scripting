#!/usr/bin/env python3.7

S1="Python"
print(S1.islower())
print(S1.isupper())
print(S1.startswith('p'))
print(S1.startswith('P'))
print(S1.endswith('on'))
print(S1.istitle())

S2="python scripting"
S3=" "
print(S2.isspace())
print(S3.isspace())

S4="some string"
S5="324324"
print(S4.isnumeric())
print(S5.isnumeric())
