
import boto3

iam_con_res=boto3.resource(service_name='iam')
iam_con_cli=boto3.client(service_name='iam')

#List users using Resource
for each_user in iam_con_res.users.all():
    print(each_user)

# List users using Client

for each in iam_con_cli.list_users()['Users']:
    print(each)
    print(each['UserName'])

