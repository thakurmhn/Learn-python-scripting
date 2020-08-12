#!/usr/bin/env python3.7

import shutil

src='/tmp/testfile'
dest='/var/tmp/testfile.bkp'

# Copy file
shutil.copy(src,dest)


dest='/var/tmp/testfile1'
# copy file with all metadata of src file
shutil.copy2(src,dest)

# copymode - retain source file permissions 

shutil.copymode(src,dest)

## Copy file object
'''
f1=open('file1.txt','r')
f2=open('file2.txt','r')
shutil.copyfileob(f1,f2)
'''

## Copy recursively

'''
shutil.copytree('srcdir','destdir')
'''

