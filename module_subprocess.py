#!/usr/bin/env python3.7

import subprocess

'''
Syntax:

sp=subprocess.Popen(cmd,shell=True/False,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
## This takes some time to execute command
rc=sp.wait()  ## wait to run a command and get return code stored in rc

out,err=sp.communicate()
print(f"Output is {out}")
print(f"Error is {error}")

==========================
When shell=True, python opens new shell and run command within it

if shell=True commands should passed as string 'ls -ltr'
if shell=False commands to be passed as list ['ls', 'ltr']

cmd='ls -ltr'
sp=subproces.Popen('ls -ltr',shell=True,stdout=sbprocess.PIPE)
print(sp.communicate())

When shell=False, commands to be provided as list

sp=subprocess.Popen(['ls','-ltr'],shell=False,stdout=subprocess.PIPE)
print(sp.communicate())

By default command output is in byte code; To convert it into string 

sp=subprocess.Popen(['ls','-ltr'],shell=False,stdout=subprocess.PIPE,universal_newlines=True)


When to use shell=True? When want to use env variables in commands

cmd='echo $HOME'
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,universal_newlines=True)

'''

cmd='ls -ltr'
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()
print(f"Output: {out}")
print(f"Error: {err}")
print(f"Return code: {rc}")

## Print outout as list
print(f"Output: {out.splitlines()}")

print('=' * 20)
cmd=['echo', '$HOME']
sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
out,err=sp.communicate()
print(f"Output: {out}")
print('=' * 20)

cmd='echo $HOME'
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
out,err=sp.communicate()
print(f"Output: {out}")
