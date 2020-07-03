#!/usr/bin/env python3.7
'''
num=eval(input("Please enter number between range [1-10] :    "))

if num in [1,2,3,4,5,6,7,8,9,10]:

   if num==1:
       print("One")
   elif num==2:
       print("two")
   elif num==3:
       print("Three")
   elif num==4:
       print("Four")
   elif num==5:
       print("Five")
   elif num==6:
       print("Six")
   elif num==7:
       print("Seven")
   elif num==8:
       print("Eight")
   elif num==9:
       print("Nine")
   else:
       print("Ten")
else:

  print("Number is out of range, please enter number between [1-10] range")
'''

# Enhanced version
num=eval(input("Please enter number between range [1-10]:     "))

num_words={1:"one", 2:"two", 3:"three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten"}

if num in [1,2,3,4,5,6,7,8,9,10]:
    print(num_words.get(num))
else: 
    print("Number is out of range, please enter number between [1-10] range")
   
