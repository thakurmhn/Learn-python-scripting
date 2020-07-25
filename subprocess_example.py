#!/usr/bin/env python3.7

## Find java version

import subprocess

cmd='java -version'
cmd=cmd.split() ## converted cmd into list

sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
o,e=sp.communicate()
if rc==0:
    o=e
    #print(o.splitlines())
    for each_line in o.splitlines():
        if "version" in each_line: 
            print(each_line.split()[2])
else: 
    print("Command failed with errors")
