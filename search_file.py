#!/usr/bin/env python

## Finds all configuration files in /etc/ and prints their last modification time


import os
import fnmatch
import time
import datetime

path="/etc"

for r,d,f in os.walk(path):
     for each_file in f:
       if fnmatch.fnmatch(each_file, '*conf') or fnmatch.fnmatch(each_file, '*config'):
           configfile_path = os.path.join(r,each_file)
           modTimesinceEpoc = os.path.getmtime(configfile_path)
           modificationTime = datetime.datetime.fromtimestamp(modTimesinceEpoc).strftime('%Y-%m-%d %H:%M:%S')

           ## Python2 print statement
           print("{}\t\t\t\t\t\t\t{}".format(configfile_path,modificationTime))
   
           ## Python3 print statement, enable if using python3 version 
           #print(f" {configfile_path}\t\t\t\t\t\t LastModified: {modificationTime}")
   
