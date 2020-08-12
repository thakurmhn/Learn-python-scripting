#!/usr/bin/env python3.7

'''
a=eval(input("Enter number one: "))
b=eval(input("Enter number two: "))
aresult=a+b
print(f"addition of a and b is: {aresult}")
sresult=a-b
print(f"subtraction of a and b is: {sresult}")
'''

# put the above code in functions

def addition(m,n):  # a=m b=n
    aresult=m+n
    print(f"addition of m and n is: {aresult}")
    return None

def subtraction(p,q):  # a=p b=q
    sresult=p-q
    print(f"subtraction of p and q is: {sresult}")
    return None

# call the functions in main()

def main():
   a=eval(input("Enter number one: "))
   b=eval(input("Enter number two: "))
   addition(a,b)      # this is equivalant to addition(4,2); passing value of a and b to addtion function as positional parameters
   subtraction(b,a)   # this is equivalant to subtracction(18,6); reversed the postion of argument
   return None 


main()
