# function to create client

import boto3

def create_session(profile='default', region='us-east-1'):
    session=boto3.session.Session(profile_name=profile, region_name=region)
    return session

def create_resource(service_name):

    aws_session=create_session()
    if service_name == 'iam':
        iam_resource = aws_session.resource('iam')
        return iam_resource
    elif service_name == 's3':
        s3_resource = aws_session.resource('s3')
        return s3_resource
    elif service_name == 'ec2':
        ec2_resource = aws_session.resource('ec2')
        return ec2_resource 



def usage_demo():
    iam_res=create_resource('iam')
    s3_res=create_resource('s3')
    ec2_res=create_resource('ec2')

    print(dir(s3_res))
    print(dir(iam_res))
    print(dir(ec2_res))


if __name__ == '__main__':
    usage_demo()











