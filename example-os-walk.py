#!/usr/bin/env python3.7

import os

path='/root/python-learning'

for r,d,f in os.walk(path):

#    print(f)

    if len(f) != 0:
        print(r)
        for each_file in f:
            print(os.path.join(r,each_file))
            print('-------------------------------------')
