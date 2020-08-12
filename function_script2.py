#!/usr/bin/env python3.7


import function_script1

# print(dir(function_script1))
# print(__name__)

def multiply(m,n):
    print(f"multiplication of m and n is : {m*n}")
    return None

def main():
    x=7
    y=8
    function_script1.addition(x,y)   ## Calling function from function_script1
    multiply(x,y)
    return None


if __name__=="__main__":
    main()
