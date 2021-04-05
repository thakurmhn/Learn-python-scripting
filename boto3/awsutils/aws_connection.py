import boto3
import os

def aws_con():
    aws_profile=os.getenv("AWS_PROFILE")
    mgmt_con=boto3.session.Session(profile_name=aws_profile)

aws_con()





