#!/usr/bin/env python3.7

'''
## Exceptions whiles changing dir
FileNotFoundError
NotADirectoryError
PermissionError
'''


import os

target_path=input("Enter target path to change: ")
print("current working directory is", os.getcwd())

try: 
    os.chdir(target_path)
    print("Working directory is changed as", os.getcwd())
except FileNotFoundError:
    print("Given path is not valid path; cant change directory")
except NotADirectoryError: 
    print("Path is not directory path")
except PermissionError:
    print("You have insufficient permissions to change directory")
except Exception as e: 
    print(e)

