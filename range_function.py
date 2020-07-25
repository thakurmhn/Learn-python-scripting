#!/usr/bin/env python3.7

## Range works differrently in Python2


print(list(range(5)))

'''
sysntax: range(start,stop,step)

if sigle number is passed to range it is stop value and default start=0, stop=1

'''

print(list(range(0,20,1))) ## last number will be  stop value - 1

print(list(range(0,21,2)))
print(list(range(0,31,3)))


print(list(range(10,2)))

print(list(range(10,2,-1)))
print(list(range(10,0,-1)))

print(list(range(-2,-10)))
print(list(range(-2,-10,-1)))


my_list = [2,4,5,3,'hello']

print(list(range(len(my_list))))


for each_index in range(len(my_list)):

     print(f"Index{each_index} ---> has value ---> {my_list[each_index]}")
