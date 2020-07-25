#!/usr/bin/env python

import os
import subprocess

threshold='60'

cmd='df -h'
cmd=cmd.split()

sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
o,e=sp.communicate()

if rc==0:
    for each_line in o.splitlines():
        if not "tmpfs" in each_line or "devfs" in each_line:
            print(each_line)
