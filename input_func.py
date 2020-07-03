#!/usr/bin/env python3.7
'''
x=input("Enter value of x: ")  ## Entered values will be considered as string by input method
y=input("Enter value of y: ")

print(f"value of x is {x} and value of y {y} and they are datatype of {type(x)}")

## Covert to integer

x=int(input("Enter value of x: "))
y=int(input("Enter value of y: "))

print(f"Addition of {x} and {y} is {x+y} ")

## Use of eval() - eval itself identyfies datatypes whether its int of flot or string 
## incase of string while passing, pass in qoutes like "somestring"
'''
x=eval(input("Enter value of x: "))
y=eval(input("Enter value of y: "))
print(f"Addition of {x} and {y} is {x+y} ")
