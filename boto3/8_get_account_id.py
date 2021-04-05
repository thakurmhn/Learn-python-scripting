# Get account id
# This is very usefull while working with multiple aws accounts

import boto3
mgmt_con=boto3.session.Session(profile_name='default')
sts_con_cli=mgmt_con.client(service_name='sts', region_name='us-east-1')
response=sts_con_cli.get_caller_identity()
print(response.get('Account'))  # respose is dict output
# OR
print(response['Account'])



