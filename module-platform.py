#!/usr/bin/env python3.7

import platform as pt

'''
print(dir(pt))
print(help(pt))
'''
print(f"This is {pt.system()} Host")
print(f"OS relese is {pt.release()}")
print(f"Python version is {pt.python_version()}")
print(f"Python major, minor version is {pt.python_version_tuple()}")
print(f"Installed processor is {pt.processor()}")
print(f"System Architechture is {pt.architecture()}")
print(f"Node info: {pt.node()}")
print(f"Uname info: {pt.uname()}")
