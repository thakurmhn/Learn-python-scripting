#!/usr/bin/env python3.7

value = 4
'''
while value <= 8765:
    print(value)
    value = value+4
'''

'''
count = 1
while count <=5: 
    print("hello")
    count = count+1
'''

## break keyword
'''
count = 1
while count <= 15:
    print(count)
    count = count+1
    if count == 8:
        break
'''

# Continue Keyword - skip the lines of block in that itteration , e.g if it matches 7 print statement will be skipped. 

for each in range(1,11):
    if each == 7:
        continue ## Contine next itteration if each == 7
        print("This line will be skipped as it is part of contine statement")
    print(each)

## pass keyword  -- for testing, avoid error conditions if no statement written under loop of if statement

for each in range(1,11):
    pass

if True: 

    pass
    
