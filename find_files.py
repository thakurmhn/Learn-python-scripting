#!/usr/bin/env python3.7

## Finds files based on extenstions 

import os

f_path = input("Please Enter Path: ")

if os.path.isfile(f_path):
   print("Provided path is not directory path")

else: 
   f_flist=os.listdir(f_path)
   if len(f_flist) == 0:
       print("Path is empty directory")

   f_ext = input("Please enter file extension, eg. .py/.txt/.log: " )

   list_out = []
   for each_file in f_flist:
   
       if each_file.endswith(f_ext):
           list_out.append(each_file)
           
   if len(list_out) == 0:
      print("Files not found")
   else:     
       print(list_out)
 
