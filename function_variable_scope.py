#!/usr/bin/env python3.7


def func1(): 
    x=50   # local variable
    print("This is the x value from func1:", x)
    return None

def func2(y):   # value of y is deriving from main() x=10; here y' is Parameter to the function
    print("This is the x value from func2:", y)
    return None
'''
x=40    # Global variable; can be accessed by func2

func1()
func2()
'''

# Calling function from another function 

def main():
# There are two ways pass x value to func2(); 1. define x as global var or pass x as Argument to func2()
    # global x
    x=10     ## x is local variable to main() to be passed to func2; 
    func1()
    func2(x) # 10 valune is being passed to func2() y=10; Here x is called Argument to the function

main()
