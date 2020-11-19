import os
import sys
import random

class AWS:
    def ConfigureAWSCLI(self):
        os.system('clear')
        os.system("aws configure --profile myprofile")

    #AWS EC2 Menu
    def AWSEC2(self):
        os.system('clear')
        while True:
            os.system("clear")
            print("""----------- AWS EC2 Menu-------------\n\n
Press 1 : To create New Instance (Custom Name)
Press 2 : To create ONE TAP instance 
Press 3 : To list the available instances
Press 4 : To stop any running instance
Press 5 : To Create new instance (according to your requirements)
Press 6 : To go back
Press exit : To exit""")
            print('\n')
            choice=input("Enter Your Choice : ")
            
            if ("exit" in choice) or ("back" in choice):
                exit("Exiting...")
            
            elif choice=="1":
                print("\nInstances already Available: \n")
                os.system("aws ec2 describe-instances --filters Name=tag-key,Values=Name --query \"Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key=='Name']|[0].Value}\" --output text")
                iname=input("Instance Name: ")
                os.system(f"aws ec2 run-instances --image-id ami-052c08d70def0ac62 --instance-type t2.micro --count 1 --subnet-id subnet-878d87ef --security-group-ids sg-0c3b45eedda355852 --tag-specifications ResourceType=instance,Tags=[{{Key=Name,Value={iname}}}] --key-name keytest1")

            elif choice=="2":
                x = ''.join((random.choice(string.ascii_letters) for i in range(5)))
                x += ''.join((random.choice(string.digits) for i in range(3)))
                x=list(x)
                random.shuffle(x)
                iname=''.join(x)
                os.system(f"aws ec2 run-instances --image-id ami-052c08d70def0ac62 --instance-type t2.micro --count 1 --subnet-id subnet-878d87ef --security-group-ids sg-0c3b45eedda355852 --tag-specifications ResourceType=instance,Tags=[{{Key=Name,Value={iname}}}] --key-name keytest1")
		
            elif choice=="3":
                print("\n Available Instances: \n")
                os.system("aws ec2 describe-instances --filters Name=tag-key,Values=Name --query \"Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key=='Name']|[0].Value}\" --output text")
                view=input("\n Want detailed view? [y/n] :")
                if 'y' in view:
                    os.system("aws ec2 describe-instances --output table")
                elif "n" in view:
                    continue
                else:
                    print("Invalid Input. Proceeding..")
            
            elif choice=="4":
                print("\n Available Instances: \n")
                os.system("aws ec2 describe-instances --filters Name=tag-key,Values=Name --query \"Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key=='Name']|[0].Value}\" --output text")
                print("\nYou can copy paste id from this list.\n")
                eid=input("Enter Instance Id to be stopped: ")
                os.system(f"aws ec2 stop-instances --instance-ids {eid}")	
            
            elif choice=="5":
                print("\nNote: Enter exact details otherwise operation might fail.\n")
                print("""Commonly Used Images: 
Amazon Linux 2 - ami-0e306788ff2473ccb
Red Hat (RHEL8) - ami-052c08d70def0ac62
SUSE Linux Server 15 SP2 - ami-0d0522ed4db1debd6
Ubuntu Server 20.04 - ami-0cda377a1b884a1bc
MS Windows Server 2019 - ami-0b2f6494ff0b07a0e""")
		   
                image=input("Image Id: ")
                typee=input("Instance Type: ")
                count=input("Number of instance: ")
                tag=input("Name of Instance: ")
                print("Available Keys: \n")
                os.system("aws ec2 describe-key-pairs --key-name")
                key=input("Key name: ")
                print("""Commonly Used Subnets:

Mumbai:								N.Virginia:

ap-south-1a - subnet-878d87ef		us-east-1a - subnet-8c18a5ea	us-east-1d - subnet-69c77e36 
ap-south-1b - subnet-b56b10f9		us-east-1b - subnet-139a2132	us-east-1e - subnet-d104c4e0
ap-south-1c - subnet-0af47971		us-east-1c - subnet-cb5d1186	us-east-1f - subnet-4f077141
""")
                subnet=input("Enter Subnet Id: ")
                os.system(f"aws ec2 run-instances --image-id {image} --instance-type {typee} --count {count} --subnet-id {subnet} --security-group-ids sg-0c3b45eedda355852 --tag-specifications ResourceType=instance,Tags=[{{Key=Name,Value={tag}}}] --key-name {keyy}")
	
            elif choice == "6":
                self.Menu()

            else:
                print("Invalid Choice. Try Again!")
            
            input("\n\nPress Enter to continue...")
    #AWS EC2 Menu ends

    #EBS attach
    def AttachVol():
        os.system('clear')
        print("Available Volume : \n")
        os.system("aws ec2 describe-volumes --output yaml")
        print("Available Instances : \n")
        os.system("aws ec2 describe-instances --filters Name=tag-key,Values=Name --query \"Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key=='Name']|[0].Value}\" --output text")
        vol=input("Select Volume Id : ")
        instance=input("Select Instance Id : ")
        dev=input("Enter device folder to attach (Ex. /dev/sd0) : ")
        os.system(f"aws ec2 attach-volume --volume-id {vol} --instance-id {instance} --device {dev}")


    #EBS detach
    def detach():
        os.system('clear')
        print("Available Volume : \n")
        os.system("aws ec2 describe-volumes --output yaml")
        print("Available Instances : \n")
        os.system("aws ec2 describe-instances --filters Name=tag-key,Values=Name --query \"Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key=='Name']|[0].Value}\" --output text")
	


    #AWS EBS VOLUME Menu
    def EBSVol(self):
        os.system('clear')  
        while True:
            os.system("clear")
            print("""--------------EBS Volume Menu------------------\n\n
Press 1 : To create Volume
Press 2 : To show available Volumes
Press 3 : To delete volume
Press 4 : To attach/detach volume
Press 5 : To go back 
Press 6 : To go Main menu 
press exit : To exit""")

            print('\n')
            choice=input("Enter Your Choice : ")
            
            if ("exit" in choice) or ("back" in choice):
                exit("Exiting...")

            elif choice=="1":
                size=input("Size : ")
                print("""Some Availability Zones :
ap-south-1(a-c)	India (Mumbai)				ap-southeast-1(a-c)	Asia Pacific (Singapore)
us-east-1(a-f)	US East (N. Virginia)		us-west-1(a&c)	US West (N. California)
us-west-2(a-d)	US West (Oregon)			eu-west-1(a-c)	EU (Ireland)
eu-central-1(a-c)	EU (Frankfurt)			ap-northeast-1(a,c,d)	Asia Pacific (Tokyo)
""")
			
                zone=input("Availability Zone (AZ) : ")			
                print("\n\ngp2 for General Purpose SSD, \nio1 or io2 for Provisioned IOPS SSD, \nst1 for Throughput Optimized HDD, \nsc1 for Cold HDD,\nstandard for Magnetic volumes\n\n")
                vtype=input("Type of Volume : ")
                os.system(f"aws ec2 create-volume --volume-type {vtype} --size {size} --availability-zone {zone}")
                print("\n\n!!Operation Complete!! \n Updated Volume List : ")
                os.system("aws ec2 describe-volumes --output yaml")
                print("\n")
                cnf=input("Would you like to attach the created volume? [y/n] : ")
                if cnf=='y':
                    print("\nNow Let's attach this Volume.\n Select an OS to attach : \n")
                    os.system("aws ec2 describe-instances --filters Name=tag-key,Values=Name --query \"Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key=='Name']|[0].Value}\" --output text")
                    vol=input("Select Volume Id : ")
                    instance=input("Select Instance Id : ")
                    os.system(f"aws ec2 attach-volume --volume-id {vol} --instance-id {instance} --device /dev/sd2")
                elif cnf=='n':
                    print("Okay, Getting back..")
                else:
                    print("Sorry, Invalid Input.")
		
            elif choice=="2":
                print("\n All Available Volumes : \n")
                os.system("aws ec2 describe-volumes --output yaml")
	    
            elif choice=="3":
                print("\n Note: It might fail in case the volume is 'in use' or not been detached\n Available Volumes: \n")
                os.system("aws ec2 describe-volumes --output yaml")
                print("\n")
                vol=input("Enter volume id (to delete) : ")
                os.system(f"aws ec2 delete-volume --volume-id {vol}")
            
            elif choice=="4":
                print("""Press 1 : To attach volume
Press 2 : To detach Volume""")
                
                ch=input("Enter your choice : ")
                if ch=="1":
                    self.AttachVol()

                elif ch=="2":
                    self.DetachVol()
			
                else:
                    print("Invalid Input...")
		
            elif choice == "5":
                self.AWSEBS()

            elif choice == "6":
                self.Menu()

            else:
                print("Invalid Choice. Try Again!")

            input("\n\nPress Enter to continue..")


    #AWS EBS SNAPSHOT Menu
    def EBSSnap(self):
        while True:
            os.system("clear")
            print("""---------------EBS Snapshot Menu---------------\n\n
Press 1 : For listing available Snapshots
Press 2 : For creating new Snapshot
Press 3 : For deleting any Snapshot
Press 4 : To go back
Press 5 : To go main menu
Press exit : To exit""")
    
            print('\n')
            choice=input("Enter Your Choice : ")
		
            if ("exit" in choice) or ("back" in choice):
                exit("Exiting...")
		
            elif choice=="1":
                print("\n------- Available Snapshots -------\n")
                os.system("aws ec2 describe-snapshots --owner-ids self --output yaml")
		
            elif choice=="2":
                print("List of available volumes with their ID's : \n")
                os.system("aws ec2 describe-volumes --output yaml")
                print("\n")
                vol=input("Volume (Id) for creating Snapshot : ")
                name=input("Name of Snapshot : ")
                desc=input("Snapshot description : ")
                os.system(f"aws ec2 create-snapshot --volume-id {vol} --description \"{desc}\" --tag-specifications \"ResourceType=snapshot,Tags=[{{Key=Name,Value={name}}}]\" ")
                print("\n\n!!Operation Complete!!\n\n")
		
            elif choice=="3":
                inp=input("Want to view available snapshots? [y/n] : ")
                if inp=="y":
                    os.system("clear")
                    print("------- Available Snapshots -------\n")
                    os.system("aws ec2 describe-snapshots --owner-ids self --output yaml")
                    print("\n")
                else:
                    print("\n Thanks for Confirmation\n")
                    delete=input("Enter the snapshot(id) you want to delete : ")
                    os.system(f"aws ec2 delete-snapshot --snapshot-id {delete}")
                    print("\n !!Operation Complete!! \n")
		
            elif choice == "4":
                self.AWSEBS()

            elif choice == "5":
                self.Menu()

            else:
                print("Invalid Choice. Try Again!")

        input("\n\nPress Enter to continue..")

    #AWS EBS SNAPSHOT Menu ENDS


    #AWS EBS Menu
    def AWSEBS(self):
        os.system('clear')
        while True:
            os.system("clear")
            print("""-------------EBS Menu-------------\n\n
Press 1 : For service related to Volume
Press 2 : For service related to Snapshot
Press 3 : To go back
Press exit : To exit""")
            print('\n')
            choice=input("Enter Your Choice : ")
            
            if ("exit" in choice) or ("back" in choice):
                exit("Exiting...")
            
            elif choice=="1":
                self.EBSVol()
            
            elif choice=="2":
                self.EBSSnap()
            
            elif choice == "3":
                self.Menu()
            
            else:
                print("Invalid Choice. Try Again!")

            input("\n\nPress Enter to continue..")

    #AWS EBS Menu Ends

    #AWS KEY Menu
    def AWSKey(self):
        while True:
            os.system("clear")
            print("""------------------AWS KEY Menu---------------------\n\n
Press 1 : To create New Key
Press 2 : To list the available Keys
Press 3 : To delete available Key
Press 4 : To go back
Press exit : To exit""")
            
            print('\n')
            choice=input("Enter Your Choice : ")
            
            if ("exit" in choice) or ("back" in choice):
                exit("Exiting...")
            
            elif choice=="1":
                keyname=input("Enter Unique Keyname: ")
                os.system(f"aws ec2 create-key-pair --key-name {keyname}")
                print("!!Operation Complete!!")
		
            elif choice=="2":
                os.system("aws ec2 describe-key-pairs --output table")
		
            elif choice=="3":
                print("Available Keys:\n")
                os.system("aws ec2 describe-key-pairs")
                keydelete=input("Enter key name you want to delete: ")
                os.system(f"aws ec2 delete-key-pair --key-name {keydelete}")
                print("!!Operation Complete!!")
		
            elif choice == "4":
                self.Menu()
            
            else:
                print("Invalid Choice. Try Again!")
            
            input("\n\nPress Enter to continue..")

    #AWS KEY Menu ENDS

    #AWS S3 Menu
    def AWSS3(self):
        while True:
            os.system("clear")
            print("""----------------AWS S3 Menu------------------\n\n
Press 1 : To create S3 bucket
Press 2 : To delete S3 bucket
Press 3 : To list S3 bucket(s)
Press 4 : To put object into bucket
Press 5 : To list object from bucket
Press 6 : To delete object from bucket
Press 7 : To Move Object form One bucket to another
Press 8 : To Copy Object form One bucket to another
Press 9 : To go back
Press exit : To exit""")
            
            print('\n')
            choice=input("Enter Your Choice : ")
            if ("exit" in choice) or ("back" in choice):
                exit("Exiting...")
		
            elif choice=="1":
                print("\nTry to be specific because \nS3 uses unique bucket naming system. \nBuckets already available : \n\n")
                os.system("aws s3api list-buckets --output yaml")
                bname=input("Enter unique bucket name : ")
                os.system(f"aws s3 mb s3://{bname}")
                print("\n !!Opeation Complete!! \n")			
		
            elif choice=="2":
                bucket=input("Enter bucket name: ")
                os.system(f"aws s3api delete-bucket --bucket {bucket}")
                print("!!Operation Complete!!")
		
            elif choice=="3":
                print("Available Bucket(s) : \n")
                os.system("aws s3api list-buckets --output yaml")
                print("\n")
		
            elif choice=="4":
                obj=input("Enter Location of the object: ")
                buc=input("Enter Bucket name: ")
                print("----")
                os.system(f"aws s3 cp \"{obj}\" s3://{buc} ")
		
            elif choice=="5":
                os.system("clear")
                print("------- S3 Objects Listing -------")
                print("Available Buckets: \n")
                os.system("aws s3 ls")
                print("""\nNote: To view the objects of any bucket which is inside
some folder, then in such case use '/' to see the object.
Ex: If there is folder named 'LW' inside 'ARTH' bucket :
Use - ARTH/LW to view objects inside LW.""")
                while True:
                    inp=input("Enter bucket Name: ")
                    if "exit s3" in inp:
                        break
                    os.system(f"aws s3 ls s3://{inp}")
                    inpu=input("Want to peek inside some folder? [y/n] :")
                    if inpu=='y':
                        folder=input("Write folder path: ")
                        os.system(f"aws s3 ls s3://{inp}/{folder}")
                    
                    elif inpu=='n':
                        print("Geting back...")
                        break
				
                    else:
                        print("Invalid Input.")
                        break
                    
            elif choice=="6":
                os.system("aws s3 ls")
                print("")
                bucket=input("Enter Bucket Name: ")
                print("\nNote: Enter path of object in case the location of file is \nunder subfolder of root S3 bucket(folder).\n")
                obj=input("Enter Object name :")
                os.system(f"aws s3api delete-object --bucket {bucket} --key {obj}")
		
            elif choice=="7":
                print("""Ex: If you want to move an object named test.txt from
mybucket to mybucket2, then give details as following:
Source Bucket Name: mybucket
Destination Bucket name: mybucket2
Object name: test.txt 
(If obj is located inside any folder then give the path.) \n
Available Buckets: """)
                os.system("aws s3 ls")
                print(" ")
                bucket1=input("Source bucket name: ")
                bucket2=input("Destination bucket name: ")
                obj=input("Object name: ")
                cnf=input("Store in root folder of Destination bucket? [y/n]: ")
                if cnf=='y':
                    print(" ")
                    os.system(f"aws s3 mv s3://{bucket1}/{obj}  s3://{bucket2}/")
			
                elif cnf=='n':
                    folder=input("Folder name of Destination bucket: ")
                    print("")
                    os.system(f"aws s3 mv s3://{bucket1}/{obj}  s3://{bucket2}/{folder}/")
                else:
                    print("Invaid input")
                
            elif choice=="8":
                print("""Ex: If you want to copy an object named test.txt from
mybucket to mybucket2, then give details as following:
Source Bucket Name: mybucket
Destination Bucket name: mybucket2
Object name: test.txt 
(If obj is located inside any folder then give the path.) \n
Available Buckets: """)
                os.system("aws s3 ls")
                print(" ")
                bucket1=input("Source bucket name: ")
                bucket2=input("Destination bucket name: ")
                obj=input("Object name: ")
                cnf=input("Store in root folder of Destination bucket? [y/n]: ")
                if cnf=='y':
                    print(" ")
                    os.system(f"aws s3 cp s3://{bucket1}/{obj}  s3://{bucket2}/")
                
                elif cnf=='n':
                    folder=input("Folder name of Destination bucket: ")
                    print("")
                    os.system(f"aws s3 cp s3://{bucket1}/{obj}  s3://{bucket2}/{folder}/")
		
                else: 
                    print("Invalid input")
            
            elif choice == "9":
                self.Menu()
                
            else:
                print("Invalid Choice. Try Again!")

            input("\n\nPress Enter to continue..")

    #AWS S3 Menu ENDS

    #AWS SECURITY GROUP Menu
    def AWSSG(self):
        while True:
            os.system("clear")
            print("""-----------------Security Group Management Menu-------------------\n\n
Press 1 : To Show Available Security Groups
Press 2 : To create Security Groups
Press 3 : To delete Security Groups
Press 4: To go back
Press exit: To exit""")
            
            print('\n')
            choice=input("Enter Your Choice : ")
            
            if ("exit" in choice) or ("back" in choice):
                exit("Exiting...")
		
            elif choice=="1":
                os.system("aws ec2 describe-security-groups --filters --query \"SecurityGroups[*].{Name:GroupName,ID:GroupId}\" --output table")
            
            elif choice=="2":
                name=input("Security Group name :")
                grp=input("Group name : ")
                disc=input("Group description : ")
                os.system(f"aws ec2 create-security-group --group-name {grp} --description {disc} --tag-specifications ResourceType=security-group,Tags=[{{Key=Name,Value={name}}}] --output yaml")
                print("\n Now, let's add some inbound rule to this group created.\n")
                sgid=input("Group-Id(which is created now): ")
                print("\nValid Protocol = tcp|udp|icmp|all or any valid protocol number\n")
                prot=input("Enter the name of protocol : ")
                port=input("Port Number : ")
                cidr=input("Allowed IP ( Ex. 0.0.0.0/0 ) : ")
                os.system(f"aws ec2 authorize-security-group-ingress --group-id {sgid} --protocol {prot} --port {port} --cidr {cidr}")
                print("!!Operation Complete!! \n Updated List : \n")
                os.system("aws ec2 describe-security-groups --filters --query \"SecurityGroups[*].{Name:GroupName,ID:GroupId}\" --output table")
		
            elif choice=="3":
                print("Available Security Groups : \n")
                os.system("aws ec2 describe-security-groups --filters --query \"SecurityGroups[*].{Name:GroupName,ID:GroupId}\" --output table")
                sgid=input("Enter Id of SG to be deleted: ")
                os.system(f"aws ec2 delete-security-group --group-id {sgid}")
                print("!!Operation Complete!! \nUpdated SG's : \n")
                os.system("aws ec2 describe-security-groups --filters --query \"SecurityGroups[*].{Name:GroupName,ID:GroupId}\" --output table")
	    
            elif choice == "4":
                self.Menu()
            
            else:
                print("Invalid Choice. Try Again!")
		
            input("\n\nPress Enter to continue..")

    #AWS SECURITY GROUP Menu ENDS

    #AWS Main Menu
    def Menu(self):
        while True:
            os.system("clear")
            print("----------- AWS Main Menu------------")
            print("""Press 1 : For working on instances
Press 2 : For working on EBS (volumes)
Press 3 : For working on Keys
Press 4 : For working on S3
Press 5 : For IAM User Management(Only if you have permission)
Press 6 : To re-configure AWS CLI console
Press 7 : To manage Security Group
Press exit: To exit""")
	
            print('\n')
            choice=input("Enter Your Choice : ")

            if ("exit" in choice) or ("back" in choice):
                exit("Exiting...")
            
            elif choice=="1":
                self.AWSEC2()
            
            elif choice=="2":
                self.AWSEBS()
            
            elif choice=="3":
                self.AWSKey()

            elif choice=="4":
                self.AWSS3()

            elif choice=="5":
                self.AWSIAM()

            elif choice=="6":
                self.ConfigureAWSCLI()

            elif choice=="7":
                self.AWSSG()

            else:
                print("Invalid Choice. Try Again!")

            input("\nPress Enter to continue..")
    
    #AWS Main Menu end

