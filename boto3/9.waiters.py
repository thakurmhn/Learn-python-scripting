## Waiter is a way to block until certain state is reached

## Example of waiter in Resouce object

import boto3

mgmt_con=boto3.session.Session(profile_name="default")
ec2_con_res=mgmt_con.resource(service_name="ec2", region_name="us-east-1")

instance_obj=ec2_con_res.Instance("i-01601a1f7e2b793c9")
print("Starting Instance ...........")
instance_obj.start()
## Implementing Waiter
instance_obj.wait_until_running()
print("Instance is now Running")