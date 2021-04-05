# Implementation of waiter in Client object
# Refer to boto3 documentation Ec2>>Waiters

import boto3

mgmt_con=boto3.session.Session(profile_name="default")
ec2_con_cli=mgmt_con.client(service_name="ec2", region_name="us-east-1")

print("Starting Instance")
response=ec2_con_cli.start_instances(InstanceIds=['i-01601a1f7e2b793c9'])
#implementing waiter
#Create waiter object
waiter=ec2_con_cli.get_waiter('instance_running.....')
waiter.wait(InstanceIds=['i-01601a1f7e2b793c9'])  #Using only InstanceIds argument
print("Instance is now running")

