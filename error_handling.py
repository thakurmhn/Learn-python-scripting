#!/usr/bin/env python3.7

'''
There are two kind of errors: 
	Syntax Errors: 		No way to handle these errors
	Exceptions or Runtime Errors :  There is way to handle these errors

try: 

   python will execute this block and see if encouters any error

except: 
  If in case of errors in above block, this block will be executed

Example exceptions

IndexError
ZeroDivisionError
ImportError
ValueError
TypeError
FileNotFoundErro
NameError
IOError

'''

try: 
    #print(4/2)
    print(4/0)
except: 
    print("Zero division error")  # ZeroDivision error

try: 
    fo=open('somefile.txt','r')
    print(fo.read())
    fo.close()
except Exception as e: 
    print(e)  ## FileNotfound Error

my_list=[1,2,3,4]

try: 
    print(my_list[4])
except Exception as e:
    print(e)
print("Continue to run next block after error")

try: 

    import fabric
except Exception as e:
    print(e)
print("Continue to run next block after error")


