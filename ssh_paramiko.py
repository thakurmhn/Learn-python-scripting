#!/usr/bin/env python3.7

import paramiko

# create ssh client 
ssh=paramiko.SSHClient()
# set StrictHostKeyCheking=No
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Connect
ssh.connect(hostname='192.168.56.110',username='root',password='*****',port='22')
## Connect using private_key
#ssh.connect(hostname='192.168.56.110',username='root',key_filename='path_to_private_keyfile',port='22')


stdin, stdout, stderr = ssh.exec_command('uptime')

# stdin, stdout and stderr are file objects
# stdin can be used to pass input to the command such as sudo password

print("Command Output is :")
print(stdout.readlines())
#print(stdout.read())/[


print("Command Error is : ")
print(stderr.readlines())

ssh.close()
