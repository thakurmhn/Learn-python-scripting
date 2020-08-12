#!/usr/bin/env python3.7

def addition(m,n):
    result=m+n
    return result

def main():

    a=eval(input("Enter number one: "))
    b=eval(input("Enter number two: "))
    #addition()
    newresult=addition(a,b) # Function retruns result after passing arguments to it. 
    print(f"Addition of a and be is: {newresult}")

main()
