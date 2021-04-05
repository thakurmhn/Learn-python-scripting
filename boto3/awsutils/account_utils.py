
import boto3
import os

aws_profile=os.getenv("AWS_PROFILE")


class AwsClient:
    def __init__(self, profile=None, region_name="us-east-1", role_arn=None):
        self.profile=profile
        self.region=region_name
        self._role_arn=role_arn

    def mgmt_con(self):


    def resource(self, aws_service_res):
        self.aws_service=aws_service_res


    def client(self, aws_service_cli):
        self.aws_service=aws_service_cli
        return self.aws_service


#aws_client=AwsClient(aws_profile)

#print(dir(aws_client))