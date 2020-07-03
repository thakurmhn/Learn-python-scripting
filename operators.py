#!/usr/bin/env python3.7

'''
Arithematic Operators  = input values and output will be values

Addition +
Subtraction -
Multiplication *
Division /
Modulo %
Floor Diviosn //
Exponential **

Assignment Operators   = input values and output will be values
Comparison Operators   = input values and output will be True or False
Identity Operators     = input values and output will be True or False
Membership Operators   = input values and output will be True or False
Logical Operators      = input True or False output will be True or False
Bitwise Operator       = Input values, perform operation on its binary and outputs values

'''


### Identity operation eg
## Identity operator compare type() of object whether its int, str, etc

## they are "is" and "is not"
'''
a=4
b=7

x="hi"

print(type(a) is type(b))
print(type(a) is type(x))
print(type(a) is not type(x))
'''
'''
## Membership operators 
## "in" and "not in" operators

valid_java=['1.6','1.7','1.8','1.9']
inst_ver='1.5'

if inst_ver in valid_java:
    print("host is deployed with valid java version")
else:
    print("host is deployed with invalid java version")
'''


## Logical operators
## "and", "or", "not" operators

# and - if any one of the condition is false, result is false
# or - if any one of the condition is true, result is true
# not - inverse true to false, False to true
print(1<2 and 2<3 and 3<4)
print(1<2 and 2<3 and 4<3)

print(not 1<2)
print(not 4<3)

## Multiple and conditions

print(1<2 and 2<3 and 3<4 and 4<5 and 5<6)

## use all() 
## all() == and operator 
print(all([1<2,2<3,3<4,4<5,5<6]))

## Multiple 'or' conditions
## use any()
## any() == or

print(any([2<3,3<4,10<7]))
