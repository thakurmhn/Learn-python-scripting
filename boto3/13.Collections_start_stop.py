import boto3

mgmt_con = boto3.session.Session(profile_name='default')
ec2_res=mgmt_con.resource('ec2', region_name='us-east-1')
ec2_cli=mgmt_con.client(service_name='ec2', region_name='us-east-1')

# Print all instances

all_instances=ec2_res.instances
'''
for each_inst in all_instances:
    print(each_inst.id)

'''
# Filter based on Tags
# Create Filter object

F1 =  {
            'Name': 'tag:Name',
            'Values': [
                'Non-Prod',
            ]
        }
# Create Waiter

# Filter only instances with tag Non-Prod
for each_nonprd in all_instances.filter(Filters=[F1]):
    #print(each_nonprd.id)
    print(f"Starting Non-Prod Instance {each_nonprd.id}")
    each_nonprd.start()
    each_nonprd.wait_until_running()
    print(f"Non-Prod Instance {each_nonprd.id} started successfully")


