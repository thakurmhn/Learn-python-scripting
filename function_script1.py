#!/usr/bin/env python3.7

def addition(a,b):
    print(f"Addition of a and b is {a+b}")
    return None

def substraction(a,b): 
    print(f"substraction of a and be is {a-b}")
    return None

'''
x=7
y=4

addition(x,y)
substraction(x,y)
multiply(x,y)
'''

def main():
    x=7
    y=4
    addition(x,y)
    substraction(x,y)
    multiply(x,y)
'''
main()
'''
#print(__name__)

if __name__=="__main__":  ## If above functions will called from another script, main() will not executed through another script
    main()                ## Functions in this script become reusable by other scritps if __name__ is used to run this script

