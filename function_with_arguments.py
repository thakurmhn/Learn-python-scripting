#!/usr/bin/env python3.7

# simple code
'''
num=eval(input("Enter your number: "))
result=num+10
print(f"Your result is : {result}")

'''

def result(num): 
    result=num+10
    print(f"Your result is : {result}")


def main():
    #global num
    num=eval(input("Enter your number: "))
    result(num)

main()   
