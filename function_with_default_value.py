#!/usr/bin/env python3.7

def display(a=1):   # default value is set as 1; if no value passed to the function default value will be printed
    print(f'Value of a is: ', a)


display(3)
display(5)
display()   ## no value passed so it will print default value here which is 1


def addition(a,b=0):  # in case of positional argument defualt value should be assigned to second parameter or it will produce syntax error
    result=a+b
    print("Result is :", result)
    return None

addition(4,5)
addition(6,8)
addition(2)



