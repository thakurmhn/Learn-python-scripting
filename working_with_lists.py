#!/usr/bin/env python3.7
'''
L=[]
print(bool(L))

L=[1,'python',23,5]
print(bool(L))

#### note: bool of empty list is always False

print(dir(L))

print(L.index(23))

#in case of duplicate value search the index
L1=[2,3,4,5,2,4,5,3,3,5]
print(L1.index(5))
print(L1.index(5,4)) # first 5 at index 3 so for next 5 search form index 4

print(L1.count(4))

print(L1.clear())

## Copy List
L2=[1,2,3,4,6]

L3=L2   # copy list with same memory address
print(id(L3))

L3=L2.copy()  # Creates new mem location
print(id(L3))

'''
'''
L=[1,3,5,7,9]
L.append(45)   ## Appends 45 at the end of the list
print(L)
L.insert(1,56) ## Insert between  index 0 and 1
L2=[8,9]
L.append(L2)
print(L)
L.extend(L2)
print(L)
'''
'''
L=[1,3,5,7,9]
L.remove(5)  ## removes valune not index number
print(L)

L.pop()
print(L.pop())
print(L)
'''

L=[3,2,4,1,7,9,6,5]
#L.sort()
#print(L)
#L.reverse()
#print(L)
L.sort(reverse=True)  ## sortcut to above 
print(L)






