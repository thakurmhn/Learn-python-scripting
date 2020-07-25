#!/usr/bin/env python3.7

import platform
import os
import time

# e.g 1

def welcome_msg():
    print("Welcome")
    return None

def hello(): 
    print("Hello")
    return None

def world():
    print("World")
    return None

welcome_msg()
hello()
world()

# eg-2
def mycode(cmd1,cmd2):
    print("Wait for a sec before executing commands")
    time.sleep(5)
    os.system(cmd1)
    print("Wait for sec befor executing second command")
    time.sleep(5)
    os.system(cmd2)

if platform.system()=="Windows":
    mycode('cls','dir')
if platform.system()=="Linux":
    mycode('clear','ls -ltr')



def display(num1,num2):
    print(f"Number one is number {num1}")
    print(f"Number two is number {num2}")

# eg-3
display(2,3)
