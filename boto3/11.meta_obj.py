import boto3

'''
meta object is useful while switching from resource to client object. 
As resource object does not provide all low level functions
e.g in below example describe_region function is not available in resource.

'''

mgmt_con = boto3.session.Session(profile_name='default')
ec2_con = mgmt_con.resource(service_name='ec2')

all_regions = ec2_con.meta.client.describe_regions()['Regions']  # List output

for region in all_regions:
    #print(region)
    print(region['RegionName'])