#!/usr/bin/env python3.7

## os.path is sub-module of os
## used to work on paths to see timestamp, type of file etc


import os

print(dir(os.path))
print(os.path.sep)


path = "/root/python-learning/module-sys.py"
path2 = "/root/python-learning/module-os.py"

print(os.path.basename(path)) ## parameter path is path variable defined above
print(os.path.dirname(path))
print(os.path.join(path,path2))
print(os.path.split(path))
print(os.path.exists(path))

if os.path.exists(path):
    print(f"{path} exist on this host")
else:
    print(f"{path} does not exist")

