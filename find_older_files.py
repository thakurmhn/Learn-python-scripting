#!/usr/bin/env python3.7

## Find x days older files in given path

import os
import sys
import datetime

target_path=input("Enter your path: ")
if not os.path.exists(target_path):
    print("Please provide valid path")
    sys.exit(1)
if os.path.isfile(target_path):
    print("Provided path is not a directory path!!")
    sys.exit(2)

file_age=eval(input("Enter file age,(find number of days older files):  "))

today=datetime.datetime.now()  ## created a class object
#print(type(today))

for each_file in os.listdir(target_path): 
    each_file_path=os.path.join(target_path,each_file)
    if os.path.isfile(each_file_path):
        #print(each_file_path,datetime.fromtimestamp(os.path.getctime(each_file_path)))
        f_creation_date=datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
        #print(dir(today - f_creation_date))
        #print(each_file_path,(today - f_creation_date).days)
        diff_age=(today - f_creation_date).days
        if diff_age > file_age: 
            #print(f"{each_file_path}  is {(today - f_creation_date).days} old")
            print(each_file_path)
