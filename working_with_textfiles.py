#!/usr/bin/env python3.7

'''
create new file ==> w
append to file ===> a
read from file ==> r
'''

# Create a txt file
fo=open('demo.txt','w')  ## Create class object fo
fo.write("This is line\n")
fo.write("This is second line\n")
fo.write("This is third line")
fo.close()

# writelines()

fo=open('demo1.txt','w')
fo.writelines(["line1\n", "line2\n", "line3\n"])
fo.close()


## Write lines using for loop

lines=["line1", "line2", "line3"]

fo=open('demo_loop.txt','w')
for each_line in lines: 
    fo.write(each_line+"\n")
fo.close()

## Read the file
fo=open('demo_loop.txt','r')
content=fo.read()    
print(content)
fo.close()


## readlines()

fo=open('demo_loop.txt','r')
print(fo.readlines()) 		#provides list of lines
fo.close()

## Print first 2 lines

fo=open('demo_loop.txt','r') 
content=fo.readlines()
for each_index in range(2):
    print(content[each_index])
fo.close()

# print last line
print(content[-1])

## Copy file content to another file
fs=open('demo_loop.txt','r')
content=fs.read()
fs.close()

fd=open('demo_copy.txt','w')
fd.write(content)
fd.close()

fd=open('demo_copy.txt','r')
print(fd.read())

'''
fs=open('demo_loop.txt','r')
fd=open('demo_copy.txt','w')

scontent=fs.readlines()
for each in scontent: 
    fd.write(each)
fs.close()
fd.close()
fr=open('demo_copy.txt','r')
print(fr.read())
'''


