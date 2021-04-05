# how to use Iam resouces using resource objec
import boto3
mgmt_con=boto3.session.Session(profile_name='default')

iam_con=mgmt_con.resource(service_name='iam', region_name='us-east-1')
ec2_con=mgmt_con.resource(service_name='ec2', region_name='us-east-1')
s3_con=mgmt_con.resource(service_name='s3',region_name='us-east-1')

# Refer to documentation and see how to use each resource object

# Print all users
response=iam_con.users.all() # iterator object
for each_user in response:
    print(each_user.name)

# Limit users
user_iterator = iam_con.users.limit(
    count=2
)

for each in user_iterator:
    print(each.name)

# List all ec2 instances
instance_iterator = ec2_con.instances.all()

for each_item in instance_iterator:
    #print(each_item)  # This is object
    print(each_item.id)

# List all S3 buckets

bucket_iterator = s3_con.buckets.all()
for each_bucket in bucket_iterator:
    print(each_bucket.name)

