#!/usr/bin/env python3.7

'''
In case of default aws profile, no need to create mgmt console and step 1 can be skipped
'''

import boto3

#step1
# Custom Session
##aws_mgmt_con=boto3.session.Session(profile_name='default')

#step2
iam_con=boto3.resource(service_name='iam')

#step3
for each_user in iam_con.users.all():
    print(each_user.name)




