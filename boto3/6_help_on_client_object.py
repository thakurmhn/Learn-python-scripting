import boto3

#Refer to boto3 documentation >> Available Services

# Create mgmt console
mgmt_con=boto3.session.Session(profile_name='default')  # Can specify any awscli profile

# Create Iam console using client object
iam_con_cli=mgmt_con.client(service_name='iam', region_name='us-east-1')

# Create Ec2 console

ec2_con_cli=mgmt_con.client(service_name='ec2',region_name='us-east-1')

# Create S3 console
s3_con_cli=mgmt_con.client(service_name='s3')

# Store the user_list in response var

response=iam_con_cli.list_users()
#print(response)  # response is a dict
print(response['Users']) # users is list




