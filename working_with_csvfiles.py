#!/usr/bin/env python3.7


import csv

# Read CSV file content

file="democsv.csv"

fo=open(file,'r')
content=csv.reader(fo,delimiter=",")  ## Default delimiter is comma, if not specified

for each in content: 
    print(each)
fo.close()


# Print Header 
fo=open(file,'r')
content=csv.reader(fo,delimiter=",")
header=(list(content))
print(f"header is: {header[0]}")
fo.close()

# Another way to print header is move cursor to next line
fo=open(file,'r')
content=csv.reader(fo,delimiter=",")
header=next(content) # copy current line at cursor to header var
print(f"header is : {header}")

# Count number of rows in file
rows=list(content)
print(f"Number of rows : {len(rows)}")
fo.close()


# Create a CSV file
fo=open('newcsv.csv','w',newline="") # in python3 have to provide newline="" or else it will append new line after every row if files is opened in excel

writer=csv.writer(fo,delimiter=",")
writer.writerow(['Sno','Name','Age'])
writer.writerow(['1','John',23])
writer.writerow(['2','Mike',45])

fo.close()


## Another way to write rows

fo=open('newcsv1.csv','w',newline="")
writer=csv.writer(fo,delimiter=",")

data=[['Sno','Name','Age'], ['1','John',23], ['2','Mike',45]]
writer.writerow(data)
fo.close()


