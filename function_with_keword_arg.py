#!/usr/bin/env python3.7

def display(a,b):
    print(f'a={a}')
    return None

display(3,4)
display(a=3,b=4)  ## Another way of passing argument to function
display(b=4,a=3)



## Function with variable length argument; Functions that accept any number of arguments 

def display1(*args):
    print(args)
    return None


display1(4)
display1(34,5,6,98,00,2)


### Function with variable keywords 

def display2(**kargs):
    print(kargs)
    return None

display2(a=34)
display2(user='root', x=5.4, motd="hi", name='john', age=23)

