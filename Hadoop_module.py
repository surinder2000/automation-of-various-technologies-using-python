#!/usr/bin/python3
import os
import getpass
import fileinput
import json
class Hadoop:
    def ConfigureMasterAWS(self):
        amiid = input("Enter AMI ID: ")
        instancetype = input("Enter instance type: ")
        filepath = "aws_master_launch/instanceLaunch.tf"

        with fileinput.FileInput(filepath, inplace = True) as f:
            for l in f:
                if "ami" in l:
                    print(f"    ami = \"{amiid}\"\n",end="")
                elif "instance_type" in l:
                    print(f"    instance_type = \"{instancetype}\"",end="")
                else:
                    print(l,end="")

        print("Started Launching.....")
        os.system("terraform init aws_master_launch/")
        os.system("terraform apply -auto-approve aws_master_launch/")
        print("Completed....")

        os.system("terraform output -json > masteroutput.json")
        with open("masteroutput.json","w") as f:
            



        

    def ConfigureSlavesAWS(self):
        pass

    def ConfigureMasterLocal(self):
        ip = input("Enter host IP: ")
        username = input("Enter user name: ")
        password = getpass.getpass() 
        namenodedir = input("Enter namenode directory name: ")
        portno = input("Enter available port number: ")
        with open('/etc/myhosts.txt', 'w') as file:        
            file.write(f"[hadoopmaster]\n{ip}  ansible_user={username}  ansible_password={password}\n")
        
        with open('/Arth_task/automation-of-various-technologies-using-python/hadoopmasterconfig/vars/main.yml','w') as file:
            file.write(f"---\n# vars file for hadoopconfig\n\nnamenodedir: {namenodedir}\nportnum: {portno}\n")
        
        print("Configuration started......")
        os.system("ansible-playbook hadoopmaster.yml")
        print("Completed.......")


    def ConfigureSlavesLocal(self):
        num = int(input("How many datanodes you want to configure: "))
        with open('/etc/myhosts.txt','w') as file:
            file.write("[hadoopslave]\n")
            for i in range(num):
                ip = input(f"Enter IP {i+1}: ")
                username = input("Enter user name: ")
                password = getpass.getpass()
                file.write(f"{ip}  ansible_user={username}  ansible_password={password}\n")
        datanodedir = input("Enter datanodes directory name: ")
        masterip = input("Enter master node ip: ")
        portno = input("Enter master port number: ")
        
        with open('/Arth_task/automation-of-various-technologies-using-python/hadoopslaveconfig/vars/main.yml','w') as file:
            file.write(f"---\n# vars file for hadoopconfig\n\ndatanodedir: {datanodedir}\nmasterip: {masterip}\nportnum: {portno}\n")

        print("Configuration started.......")
        os.system("ansible-playbook hadoopslave.yml")
        print("Completed........")

    def OnLocalSystem(self):
        while True:
            os.system('clear')
            print("""Press 1: Configure Master
Press 2: Confiure Slaves
Press 3: Back Menu
Press 4: Main Menu
Press 5: Exit""")

            ch = int(input("Enter your choice: "))
            if ch == 1:
                self.ConfigureMasterLocal()
            elif ch == 2: 
                self.ConfigureSlavesLocal()
            elif ch == 3:
                self.CreateHadoopCluster()
            elif ch == 4:
                self.Menu()
            elif ch == 5:
                exit()
            else:
                print("Invalid choice")
            con = input("Do you want to continue? (Y/N): ")

            if con == "Y" or con == "y":
                continue
            else:
                exit()

    
    def OnAWSCloud(self):
        os.system("aws configure --profile myprofile")
        os.system("export AWS_PROFILE=myprofile")
        while True:
            os.system('clear')
            print("""Press 1: Configure Master
Press 2: Confiure Slaves
Press 3: Back Menu
Press 4: Main Menu
Press 5: Exit""")

            ch = int(input("Enter your choice: "))
            if ch == 1:
                self.ConfigureMasterAWS()
            elif ch == 2: 
                self.ConfigureSlavesAWS()
            elif ch == 3:
                self.CreateHadoopCluster()
            elif ch == 4:
                self.Menu()
            elif ch == 5:
                exit()
            else:
                print("Invalid choice")
            con = input("Do you want to continue? (Y/N): ")

            if con == "Y" or con == "y":
                continue
            else:
                exit()

    def CreateHadoopCluster(self):
        while True:
            os.system('clear')
            print("Where do you want to create cluster")
            print("""Press 1: On local system
Press 2: On AWS cloud
Press 3: Back Menu
Press 4: Exit""")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                self.OnLocalSystem()
            elif ch == 2:
                self.OnAWSCloud()
            elif ch == 3:
                self.Menu()
            elif ch == 4:
                exit()
            else:
                print("Invalid choice")
                ch = int(input("Enter your choice: "))
            con = input("Do you want to continue? (Y/N): ")
            if con == "Y" or con == "y":
                continue
            else:
                break

    def AdminReport(self):
        clientip = input("Enter client IP: ")
        clientuser = input("Enter client user name: ")

        os.system(f"ssh {clientuser}@{clientip} hadoop dfsadmin -report")
    
    def UploadFiles(self):
        pass
    
    def ViewFiles(self):
        pass

    def RemoveFile(self):
        pass

    def AddDataNode(self):
        pass

    def IncreaseDecreaseHadoopNodeSize(self):
        pass

    def Menu(self):
        while True:
            os.system("clear")
            print("\n----------------Hadoop Management---------------\n")
            print("""Press 1: Create Hadoop Cluster
Press 2: Hadoop cluster report
Press 3: Upload files into cluster
Press 4: View files
Press 5: Remove file from cluster
Press 6: Add new data node
Press 7: Increase or Decrease data node size
Press 8: Exit""")

            ch = int(input("Enter your choice: "))
            if ch == 1:
                self.CreateHadoopCluster()
            elif ch == 2:
                self.AdminReport()
            elif ch == 3:
                self.UploadFiles()
            elif ch == 4:
                self.ViewFiles()
            elif ch == 5:
                self.RemoveFile()
            elif ch == 6:
                self.AddNewNode()
            elif ch == 7:
                self.IncreaseDecreaseNodeSize()
            elif ch == 8:
                exit("Exiting...")
            else:
                print("Invalid choice")
                ch = int(input("Enter your choice: "))
            con = input("Do you want to continue? (Y/N): ")
            if con == "Y" or con == "y":
                continue
            else:
                exit("Exiting...")


