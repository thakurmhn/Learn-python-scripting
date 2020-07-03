#!/usr/bin/env python3.7

my_dict={'fruit':'Apple','animal':'fox','number':1, 'mylist': [2, 3, 4], 'mytuple':(5, 6, 7), 'cars':{'ford':'figo', 'maruti':'alto'} }

## accessing dict
print(my_dict)
print('='*40)

print(my_dict['fruit'])
#OR
print(my_dict.get('fruit'))
print(my_dict.get('cars'))
print('='*40)

## Modify value of one of the key
print(my_dict)
my_dict['number']=22
print(my_dict)
print('='*40)

## Append new key and value 
my_dict['Bird']='eagle'
print(my_dict)
print('='*40)

## List all keys
print(my_dict.keys())
print('='*40)
## List all values
print(my_dict.values())
print('='*40)

## items operation
print(my_dict.items())
print('='*40)

## update dict - copy content of one dict to annother dict
D1={'sport1': 'cricket'}
D2={'sport2': 'football'}
D1.update(D2)
print(D1)
print('='*40)


## Copy operation
new_dict=my_dict
print(new_dict)
print(id(new_dict), id(my_dict))
new_dict=my_dict.copy
print(id(new_dict), id(my_dict))
print('='*40)

## pop operation - removes key/value by passing key
my_dict.pop('cars')
print(my_dict)
print('='*40)

## popitems - shows removed key/values and removes randomly
removed_item=my_dict.popitem()
print(my_dict)
print(removed_item)
print('='*40)

## dict.fromkeys operation
keys=['a','e','i','o','u']
D3=dict.fromkeys(keys)
print(D3)
D3['a']='firtst alpha'
print(D3)
print('='*40)


## setdefault operation - it will look for key, if key does not present it will update new key values but if key present it will not take any action
## Useful when  you dont know if key present or not, if not present will add new key/value
D5={}
D5.setdefault('one',1)
print(D5)

D6={'fruit': 'apple'}
print(D6)
D6.setdefault('fruit','Orange')
print(D6)
D6.setdefault('Red','Apple')
print(D6)
