import boto3

'''
how to use collections from service resource 
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#service-resource

refer to collections documentation
Collections are group of resources e.g all instances, all routetables etc

'''

mgmt_con = boto3.session.Session(profile_name='default')
ec2_con_res = mgmt_con.resource('ec2', region_name='us-east-1')

inst_collections = ec2_con_res.instances

#for each in inst_collections.all():  # inst_collections.all() is iterable object
#    print(each)

# Working with filter object in resource collections
# Create Filters
F1 =  {
            'Name': 'instance-state-name',
            'Values': [
                'running',
                'stopped'
            ]
        }

F2 = {
            'Name': 'instance-type',
            'Values': [
                't2.micro',
                ]
        }
for each in inst_collections.filter(Filters=[F1, F2]):  # filters() is iterable object
    print(each)
