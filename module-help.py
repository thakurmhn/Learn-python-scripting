#!/usr/bin/env python3.7
'''
Modules are reusable scripts, that can be imported in other  scripts.
It consist of variable, functions and classes
'''


'''
# list all installed modules

print(help("modules"))

## list functions in module

import math
print(dir(math))

print(help(math))

## Use of variable (constants) 

print(math.pi)

## Use of Functions
print(math.pow(2,3))

## Diff between From Import
'''

'''
from math import *
print(pi)  ## Do not need to write math.pi, reduced syntax
'''

'''
from math import pi,pow
print(pi)
print(pow(2,3))
'''

## Alias name for module
import math as M  # created alias as M 
print(M.pi)

## Import multiple Modules
import os
import sys
import platform

## OR 
import os,sys,platform



