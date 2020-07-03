#!/usr/bin/env python3.7

import os

'''
print(dir(os))
print(help(os))
'''

print(os.sep)
# Note on windows system provide \\ in Path instead of one \ to escape \U, \n, \t etc

print(os.getcwd())
print(os.chdir("/usr/local"))
print(os.getcwd())
print(os.listdir("/usr/local"))
#os.removedirs("/opt/test")
#os.mkdir("/opt/test")
#os.makedirs("/opt/test/tmp1/xyz/abc")  # Recursively create dir

# to remove one dir/file
# os.remove("path")
# os.removedirs("path")   # Recursively remove

print(os.environ)

print(os.getuid())
print(os.getgid())
print(os.getpid)
