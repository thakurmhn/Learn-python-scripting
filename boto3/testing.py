from awsutils.account_utils import AwsClient
import os

aws_profile=os.getenv("AWS_PROFILE")

m_con=AwsClient(aws_profile)

iam_con=AwsClient.resource('iam')


