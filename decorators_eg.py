#!/usr/bin/env python3

## Decorators are higher level functions that takes other functions as argument and also return function

# simple example

user={'user': 'john', 'access_level': 'admin'}

def has_permissions(func):
    if user.get('access_level') == 'admin':
        return func
    raise PermissionsError    

def my_function():
    return 'Password for admin pannel is 1234'


my_secure_function = has_permissions(my_function)


# Calling has_permissions()

print(my_secure_function())



## More complex example ; Actual decorators are written like this


user={'user': 'john', 'access_level': 'admin'}

def has_permissions(func):
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()
    return secure_func

def my_function():
    return 'Password for admin pannel is 1234'


my_secure_function = has_permissions(my_function)


# Calling has_permissions()

print(my_secure_function())
