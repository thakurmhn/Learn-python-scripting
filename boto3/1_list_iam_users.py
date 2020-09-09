#!/usr/bin/env python3.7

'''
Boto3 Core concepts

Session
Resource
Client
Meta
Collections
Waiters
Paginators


Resouce and client are similar but 

Resource : Is higher-level-object-oriented service access and it is available for few aws services
It retruns the object and can use .operation

Client: low-level service access; provides dictionary output and available to all aws services

Meta is to switch from Resource to Client 

'''


'''
Manual steps
1. Get AWS Console
2. Get IAM Console
       Options: user, groups, roles ... etc

'''

import boto3

#step1
aws_mgmt_con=boto3.session.Session(profile_name='default')

#step2
iam_con=aws_mgmt_con.resource('iam')

#step3
for each_user in iam_con.users.all():
    print(each_user.name)




