#!/usr/bin/env python3.7

import paramiko

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.56.110',username='root',password='*****',port='22')


# Open sftp connection 
sftp_client=ssh.open_sftp()

# help
#print(dir(sftp_client))

# Download file from remote machine
#sftp_client.chdir('/tmp')
#sftp_client.getcwd()
sftp_client.get('/tmp/test_download.txt','/var/tmp/test_download.txt') # (source,dest)

# Upload file
sftp_client.put('/var/tmp/test_download.txt','/var/tmp/test_download.txt') # (source,dest)


sftp_client.close()
ssh.close()
