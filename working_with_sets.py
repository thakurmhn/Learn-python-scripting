#!/usr/bin/env python3.7

my_set={3,5,2,5,7,4,6}
print(my_set)
print(bool(my_set))

## define blank set
new_set=set({})  ## Or else it will become dictinary 
print(bool(new_set))

print(dir(new_set))


a={3,4,5,6}
b={5,6,7,8,9}

print(a.union(b))
print(a.intersection(b))
