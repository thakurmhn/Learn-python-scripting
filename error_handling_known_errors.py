#!/usr/bin/env python3.7


try: 
    #print(a)
    #print(4+"hi")
    open('file.txt')
except NameError: 
    print("Variable not defined")
except TypeError: 
    print("Addition of numbers and string not possible")
except FileNotFoundError: 
    print("Make sure file is present")
except Exception as e: 			# To print unknown exceptions which are not listed above
    print(e)
else: 
    print("This block will execute upon no exceptions in above code")

finally: 
    print("Finally will always execute")

