#!/usr/bin/env python3.7

import getpass

'''
db_pass=getpass.getpass()
print(f"entered password is {db_pass}")


## Change passowrd prompt
db_pass=getpass.getpass(prompt="Enter DB User password:")


## getuser() reads user info from evn variables $USER, $LOGNAME etc
'''
user=(getpass.getuser())
print(f"Logged in user is : {user} ")
