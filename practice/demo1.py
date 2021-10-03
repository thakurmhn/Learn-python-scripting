import boto3


#mgmt_con = boto3.session.Session(profile_name='default')

s3_client = boto3.client('s3')
res=s3_client.list_buckets()
print(res['Owner']['DisplayName'])
print(res['Owner']['ID'])

# for each_item in res['Owner']:
     # print(each_item[])
