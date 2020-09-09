#!/usr/bin/env python3.7

import boto3

#step1 Login to aws console
aws_mgmt_con=boto3.session.Session(profile_name='default')

#step2 get s3 console
s3_con=aws_mgmt_con.resource('s3')

#step3
for each_bucket in s3_con.buckets.all():
    print(each_bucket.name)




