# Menu Driven Ec2 operations using Resource object

import boto3

mgmt_con=boto3.session.Session(profile_name='default')
ec2_con_res=mgmt_con.resource(service_name='ec2', region_name='us-east-1')
ec2_con_cli=mgmt_con.client(service_name='ec2',region_name='us-east-1')

while True:
    print("Choose from the Options")
    print("""
          1. Get Instance IDs        
          2. Start Ec2 Instance
          3. Stop Ec2 Instance
          4. Terminate Ec2 Instance
          5. Reboot Instance 
          6. Exit """)
    opts=eval(input("Please Enger your Choice:  "))
    if opts==1:
        print("Getting Instance Ids...")
        respose=ec2_con_res.instances.all()
        for each in respose:
            print(each.id)
    elif opts==2:
        print("Starting EC2 Instance.....")
        inst_id=input("Please provide instance Id: ")
        target_instance=ec2_con_res.Instance(inst_id)
        target_instance.start()
        #Implementing waiter
        target_instance.wait_until_running()
        print("Instance is now running")
    elif opts==3:
        print("Stopping EC2 Instance......")
        inst_id = input("Please provide instance Id: ")
        target_instance = ec2_con_res.Instance(inst_id)
        target_instance.stop()
        # Implementing waiter
        target_instance.wait_until_stopped()
        print("Instance is now stopped")
    elif opts==4:
        print("Terminating EC2 Instance")
        inst_id = input("Please provide instance Id: ")
        target_instance = ec2_con_res.Instance(inst_id)
        target_instance.terminate()
        target_instance.wait_until_terminated()
        print("Instance is now terminated")
    elif opts==5:
        print("Rebooting Instance")
        inst_id = input("Please provide instance Id: ")
        target_instance = ec2_con_res.Instance(inst_id)
        target_instance.reboot()
    elif opts==6:
        sys.exit()
    else:
        print("Please choose valid option number")

