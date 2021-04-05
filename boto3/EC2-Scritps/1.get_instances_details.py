# Get details of ec2 instances

import boto3
from pprint import pprint ## for JSON style output

mgmt_con=boto3.session.Session(profile_name='default')
ec2_con_cli=mgmt_con.client(service_name='ec2', region_name='us-east-1')
ec2_con_res=mgmt_con.resource(service_name='ec2', region_name='us-east-1')
response=ec2_con_res.instances.all()
response=ec2_con_cli.describe_instances()['Reservations']

print("====================Instance Details==========================")
for each_inst in response:
#    pprint(each_inst)
# above is List so use another for iteration

    for each_item in each_inst['Instances']:
        #pprint(each_item) # is a dict
        print(f"Instance ID is: {each_item['InstanceId']},\n "
              f"Image id is: {each_item['ImageId']}\n"
              f" Launch Time is: {each_item['LaunchTime']}\n"
              f" Current State is: {each_item.get('State').get('Name')}")

print("================Volume Details========================")
response2=ec2_con_cli.describe_volumes().get('Volumes')
for each_vol in response2:
    #print(each_vol['Attachments'])

    for each_attch in each_vol['Attachments']:
        
        print(
            f"Volume Instance ID is:{each_attch['InstanceId']}\n"
            f"Volume Device Name is: {each_attch['Device']}\n"
            f"Volume ID is: {each_attch['VolumeId']}\n"
            f"Current Volume State is {each_attch['State']}"
        )

    for each_vol_item in each_vol:
        #pprint(each_vol)
        print(
            f"Volume in Availability zone is: {each_vol['AvailabilityZone']}\n"
            f"Is Encrypted: {each_vol['Encrypted']}\n"
            f"Volume size is: {each_vol['Size']}"

        )