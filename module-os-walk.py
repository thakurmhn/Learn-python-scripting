#!/usr/bin/env python3.7

## os.walk() is similar to find command, walks through directories recursively

import os

path = '/root/python-learning'

print(os.walk(path))  ## by default output is generator object which can be converted into list

print(list(os.walk(path))) ## print list of tuples of each recursive path. Eeach tuple consist two lists one for dir and another for files

print('------------------------------------------------------------------')

for each in os.walk(path):
    print(each)
print('------------------------------------------------------------------')


for x,y,z in os.walk(path):  ## assigned each tupple values to variable (unpacking tupple x,y,z = (1,2,3))
    print(x)
    print('------------------------------------------------------------------')
    print(y)
    print('------------------------------------------------------------------')
    print(z)

print("++++++++++++++++++++++++++++++++++++++++++++++++++")

for x,y,z in os.walk(path):
    if len(z) != 0:
        print(x)
        for each_file in z:
            print(os.path.join(x,each_file))
