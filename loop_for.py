#!/usr/bin/env python3.7

## using list

my_list=[1,2,3,4,5]

for each in my_list:
    print(each)

## Using tuple 
print("Using tupple")
for value in ('hi', 'hello', 'world', 2, 3):
    print(value)

print("Using string")

for char in "Hello World":
    print(char)

my_str = "python"
for each_char in my_str:
    print(f"{each_char} has index number {my_str.index(each_char)}")

index=0
my_str = "Hello hello world"
for each_char in my_str:
    print(f"{each_char} has index number {index}")
    index=index+1


print("odd/even")

for each in [3,45,43,56,34,87,98,22,7,6,78,100]:

   remainder = each%2
   if remainder == 0:
       print(f"{each} is even number ")
   else: 
       print(f"{each} is odd number")


