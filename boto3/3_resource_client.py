#!/usr/bin/env python3.7

import boto3

aws_mgmt_con=boto3.session.Session(profile_name='default')

iam_con_re=aws_mgmt_con.resource('iam',region_name='us-east-2')
iam_con_cli=aws_mgmt_con.client('iam',region_name='us-east-2')


# using Resouce
#print(dir(aws_mgmt_con)) ## services available with resouces
#print(dir(aws_mgmt_con.get_available_services())) ## services available with resouces
#print(dir(iam_con_re))
#print(dir(iam_con_cli))

for each_user in iam_con_re.users.all():
        print(each_user.name)



## Using Client
print(iam_con_cli.list_users())
#print(iam_con_cli.list_users()['Users']) # print key users from dict


for each_user in iam_con_cli.list_users()['Users']:
    #print(each_user)
    print(each_user['UserName'])
