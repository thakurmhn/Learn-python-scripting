#!/usr/bin/env python3.7

## print entered string at Left/Center/Right in Title format
## script shoudl work on both windows and Linux terminals

import os
terminal_width=os.get_terminal_size().columns

x=input("Enter the String: ")
print(x.center(terminal_width).title())
print(x.ljust(terminal_width).title())
print(x.rjust(terminal_width).title())

