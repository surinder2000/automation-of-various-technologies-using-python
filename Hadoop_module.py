#!/usr/bin/python3
import os
import getpass
import fileinput
import json
from WelcomePage import WelcomePage
from Colors import Colors
class Hadoop:
    def ConfigureMasterAWS(self):
        amiid = input(" Enter AMI ID: ")
        instancetype = input(" Enter instance type: ")
        filepath = "aws_master_launch/instanceLaunch.tf"

        with fileinput.FileInput(filepath, inplace = True) as f:
            for l in f:
                if "ami" in l:
                    print(f"    ami = \"{amiid}\"\n",end="")
                elif "instance_type" in l:
                    print(f"    instance_type = \"{instancetype}\"\n",end="")
                else:
                    print(l,end="")

        print(" Started Launching.....")
        os.system("terraform init aws_master_launch/")
        os.system("terraform apply -auto-approve aws_master_launch/")
        print(" Completed....")

        os.system("terraform output -json > masteroutput.json")
        with open("masteroutput.json","r") as f:
            outputvalue = json.load(f)
        os.system("chmod 400 Hadoopmasterkey.pem")
        username = input("Enter user name: ")
        with open('/etc/myhosts.txt', 'w') as f:
            f.write(f"[hadoopmaster]\n{outputvalue['MasterPublicIP']['value']}  ansible_user={username}  ansible_ssh_private_key_file={outputvalue['MasterKeyName']['value']}.pem\n")

        namenodedir = input(" Enter namenode directory name: ")
        portno = input(" Enter available port number: ")
        
        with open('/Arth_task/automation-of-various-technologies-using-python/hadoopmasterconfig/vars/main.yml','w') as f:
            f.write(f"---\n# vars file for hadoopconfig\n\nnamenodedir: {namenodedir}\nportnum: {portno}\n")
        
        print(" Configuration started......")
        os.system("ansible-playbook hadoopmaster.yml")
        print(" Completed.......")


    def ConfigureSlavesAWS(self):
        amiid = input(" Enter AMI ID: ")
        instancetype = input(" Enter instance type: ")
        count = input(" Enter no of data nodes: ")
        filepath = "aws_slave_launch/instanceLaunch.tf"

        with fileinput.FileInput(filepath, inplace = True) as f:
            for l in f:
                if "ami" in l:
                    print(f"    ami = \"{amiid}\"\n",end="")
                elif "instance_type" in l:
                    print(f"    instance_type = \"{instancetype}\"\n",end="")
                elif "count" in l:
                    print(f"    count = \"{count}\"\n",end="")
                else:
                    print(l,end="")

        print(" Started launching...")
        os.system("terraform init aws_slave_launch/")
        os.system("terraform apply -auto-approve aws_slave_launch/")

        os.system("terraform output -json > slaveoutput.json")

        os.system("chmod 400 Hadoopslavekey.pem")
        with open('slaveoutput.json','r') as f:
            outputvalue = json.load(f)

        username = input(" Enter user name: ")
        with open('/etc/myhosts.txt', 'w') as f:
            f.write("[hadoopslave]\n")
            for i in range(count):
                f.write(f"{outputvalue['SlavePublicIP']['value'][i]}  ansible_user={username}  ansible_ssh_private_key_file={outputvalue['SlaveKeyName']['value'][i]}.pem\n")

        datanodedir = input(" Enter data node directory name: ")
        masterip = intput(" Enter master node ip: ")
        portno = input(" Enter master port number: ")
        with open('/Arth_task/automation-of-various-technologies-using-python/hadoopslaveconfig/vars/main.yml','w') as f:
            f.write(f"---\n# vars file for hadoopconfig\n\ndatanodedir: {datanodedir}\nmasterip: {masterip}\nportnum: {portno}\n")

        print(" Configuration started.......")
        os.system("ansible-playbook hadoopslave.yml")
        print(" Completed........")

    def ConfigureClientAWS(self):
        amiid = input(" Enter AMI ID: ")
        instancetype = input(" Enter instance type: ")
        filepath = "aws_client_launch/instanceLaunch.tf"

        with fileinput.FileInput(filepath, inplace = True) as f:
            for l in f:
                if "ami" in l:
                    print(f"    ami = \"{amiid}\"\n",end="")
                elif "instance_type" in l:
                    print(f"    instance_type = \"{instancetype}\"\n",end="")
                else:
                    print(l,end="")

        print(" Started launching...")
        os.system("terraform init aws_client_launch/")
        os.system("terraform apply -auto-approve aws_client_launch/")

        os.system("terraform output -json > clientoutput.json")

        os.system("chmod 400 Hadoopclientkey.pem")
        with open('clientoutput.json','r') as f:
            outputvalue = json.load(f)

        username = input(" Enter user name: ")
        with open('/etc/myhosts.txt', 'w') as f:
            f.write(f"[hadoopclient]\n{outputvalue['ClientPublicIP']['value']}  ansible_user={username}  ansible_ssh_private_key_file={outputvalue['ClientKeyName']['value']}.pem\n")

        masterip = intput(" Enter master node ip: ")
        portno = input(" Enter master port number: ")
        with open('/Arth_task/automation-of-various-technologies-using-python/hadoopclientconfig/vars/main.yml','w') as f:
            f.write(f"---\n# vars file for hadoopconfig\n\nmasterip: {masterip}\nportnum: {portno}\n")

        print(" Configuration started.......")
        os.system("ansible-playbook hadoopclient.yml")
        print(" Completed........")
        

    def ConfigureMasterLocal(self):
        ip = input(" Enter host IP: ")
        username = input(" Enter user name: ")
        password = getpass.getpass(" Enter Password: ") 
        namenodedir = input(" Enter namenode directory name: ")
        portno = input(" Enter available port number: ")
        with open('/etc/myhosts.txt', 'w') as f:        
            f.write(f"[hadoopmaster]\n{ip}  ansible_user={username}  ansible_password={password}\n")
        
        with open('/Arth_task/automation-of-various-technologies-using-python/hadoopmasterconfig/vars/main.yml','w') as f:
            f.write(f"---\n# vars file for hadoopconfig\n\nnamenodedir: {namenodedir}\nportnum: {portno}\n")
        
        print(" Configuration started......")
        os.system("ansible-playbook hadoopmaster.yml")
        print(" Completed.......")


    def ConfigureSlavesLocal(self):
        num = int(input(" How many datanodes you want to configure: "))
        with open('/etc/myhosts.txt','w') as f:
            f.write("[hadoopslave]\n")
            for i in range(num):
                ip = input(f" Enter IP {i+1}: ")
                username = input(" Enter user name: ")
                password = getpass.getpass(" Enter Password: ")
                f.write(f"{ip}  ansible_user={username}  ansible_password={password}\n")
        datanodedir = input(" Enter datanodes directory name: ")
        masterip = input(" Enter master node ip: ")
        portno = input(" Enter master port number: ")
        
        with open('/Arth_task/automation-of-various-technologies-using-python/hadoopslaveconfig/vars/main.yml','w') as f:
            f.write(f"---\n# vars file for hadoopconfig\n\ndatanodedir: {datanodedir}\nmasterip: {masterip}\nportnum: {portno}\n")

        print(" Configuration started.......")
        os.system("ansible-playbook hadoopslave.yml")
        print(" Completed........")

    def ConfigureClientLocal(self):
        with open('/etc/myhosts.txt','w') as f:
            ip = input(f" Enter IP: ")
            username = input(" Enter user name: ")
            password = getpass.getpass(" Enter Password: ")
            f.write(f"[hadoopclient]\n{ip}  ansible_user={username}  ansible_password={password}\n")
        masterip = input(" Enter master node ip: ")
        portno = input(" Enter master port number: ")
        
        with open('/Arth_task/automation-of-various-technologies-using-python/hadoopclientconfig/vars/main.yml','w') as f:
            f.write(f"---\n# vars file for hadoopconfig\n\nmasterip: {masterip}\nportnum: {portno}\n")

        print(" Configuration started.......")
        os.system("ansible-playbook hadoopclient.yml")
        print(" Completed........")



    def OnLocalSystem(self):
        while True:
            os.system('clear')
            WelcomePage().HypenLine()
            print(Colors.FG.orange,"""\n\n Press 1: Configure Master
 Press 2: Confiure Slaves
 Press 3: Confiure Client
 Press 4: Back Menu
 Press 5: Main Menu
 Press 6: Exit\n\n""",Colors.reset)

            WelcomePage().HypenLine()

            ch = int(input("\n\n Enter your choice: "))
            if ch == 1:
                self.ConfigureMasterLocal()
            elif ch == 2: 
                self.ConfigureSlavesLocal()
            elif ch == 3:
                self.ConfigureClientLocal()
            elif ch == 4:
                self.CreateHadoopCluster()
            elif ch == 5:
                self.Menu()
            elif ch == 6:
                print(Colors.FG.red,"\n Exiting...",Colors.reset)
                exit()
            else:
                print(Colors.FG.red,"\n\n Invalid choice",Colors.reset)
            con = input("\n\n Do you want to continue? (Y/N): ")

            if con == "Y" or con == "y":
                continue
            else:
                print(Colors.FG.red,"\n Exiting...",Colors.reset)
                exit()

    
    def OnAWSCloud(self):
        os.system('clear')
        os.system("aws configure --profile myprofile")
        os.system("export AWS_PROFILE=myprofile")
        while True:
            os.system('clear')
            WelcomePage().HypenLine()
            print(Colors.FG.orange,"""\n\n Press 1: Configure Master
 Press 2: Confiure Slaves
 Press 3: Configure Client
 Press 4: Back Menu
 Press 5: Main Menu
 Press 6: Exit\n\n""",Colors.reset)

            WelcomePage().HypenLine()

            ch = int(input("\n\n Enter your choice: "))
            if ch == 1:
                self.ConfigureMasterAWS()
            elif ch == 2: 
                self.ConfigureSlavesAWS()
            elif ch == 3:
                self.ConfigureClientAWS()
            elif ch == 4:
                self.CreateHadoopCluster()
            elif ch == 5:
                self.Menu()
            elif ch == 6:
                print(Colors.FG.red,"\n Exiting...",Colors.reset)
                exit()
            else:
                print(Colors.FG.red,"\n\n Invalid choice",Colors.reset)
            con = input("\n\n Do you want to continue? (Y/N): ")

            if con == "Y" or con == "y":
                continue
            else:
                print(Colors.FG.red,"\n Exiting...",Colors.reset)
                exit()

    def CreateHadoopCluster(self):
        while True:
            os.system('clear')
            WelcomePage().HypenLine()
            message = "Where do you want to create cluster"
            print(Colors.FG.green,message.center(WelcomePage.width),Colors.reset)
            WelcomePage().HypenLine()
            print(Colors.FG.orange,"""\n\n Press 1: On local system
 Press 2: On AWS cloud
 Press 3: Back Menu
 Press 4: Exit\n\n""",Colors.reset)

            WelcomePage().HypenLine()

            ch = int(input("\n\n Enter your choice: "))
            if ch == 1:
                self.OnLocalSystem()
            elif ch == 2:
                self.OnAWSCloud()
            elif ch == 3:
                self.Menu()
            elif ch == 4:
                print(Colors.FG.red,"\n Exiting...",Colors.reset)
                exit()
            else:
                print(Colors.FG.red,"\n\n Invalid choice",Colors.reset)

            con = input("\n\n Do you want to continue? (Y/N): ")
            if con == "Y" or con == "y":
                continue
            else:
                print(Colors.FG.red,"\n Exiting...",Colors.reset)
                exit()

    def AdminReport(self):
        clientip = input(" Enter client IP: ")
        clientuser = input(" Enter client user name: ")
        keyname = input(" Enter key name (If client on AWS else press enter): ")
        if keyname == "":
            os.system(f"ssh {clientuser}@{clientip} hadoop dfsadmin -report")
        else:
            os.system(f"ssh -i {keyname} {clientuser}@{clientip} hadoop dfsadmin -report")
    
    def UploadFiles(self):
        clientip = input(" Enter client IP: ")
        clientuser = input(" Enter client user name: ")
        keyname = input(" Enter key name (If client on AWS else press enter): ")
        filepath = input(" Enter file path: ")
        if keyname == "":
            os.system(f"ssh {clientuser}@{clientip} hadoop fs -put {filepath} /")
        else:
            os.system(f"ssh -i {keyname} {clientuser}@{clientip} hadoop fs -put {filepath} /")

        print("\n\n Uploaded!!")
    
    def ViewFiles(self):
        clientip = input(" Enter client IP: ")
        clientuser = input(" Enter client user name: ")
        keyname = input(" Enter key name (If client on AWS else press enter): ")
        print(" Viewing files in Hadoop cluster:-\n")
        if keyname == "":
            os.system(f"ssh {clientuser}@{clientip} hadoop fs -ls /")
        else:
            os.system(f"ssh -i {keyname} {clientuser}@{clientip} hadoop fs -ls /")


    def RemoveFile(self):
        clientip = input(" Enter client IP: ")
        clientuser = input(" Enter client user name: ")
        keyname = input(" Enter key name (If client on AWS else press enter): ")
        filepath = input(" Enter file path to remove from Hadoop cluster: ")
        if keyname == "":
            os.system(f"ssh {clientuser}@{clientip} hadoop fs -rm {filepath}")
        else:
            os.system(f"ssh -i {keyname} {clientuser}@{clientip} hadoop fs -rm {filepath}")

        print("\n\n Deleted...")

    def AddDataNode(self):
        with open('/etc/myhosts.txt','w') as f:
            ip = input(f" Enter host IP: ")
            username = input(" Enter user name: ")
            password = getpass.getpass()
            f.write(f"[hadoopslave]\n{ip}  ansible_user={username}  ansible_password={password}\n")

        datanodedir = input(" Enter datanode directory name: ")
        masterip = input(" Enter master node ip: ")
        portno = input(" Enter master port number: ")
        
        with open('/Arth_task/automation-of-various-technologies-using-python/hadoopslaveconfig/vars/main.yml','w') as f:
            f.write(f"---\n# vars file for hadoopconfig\n\ndatanodedir: {datanodedir}\nmasterip: {masterip}\nportnum: {portno}\n")

        print(" Configuration started.......")
        os.system("ansible-playbook hadoopslave.yml")
        print(" Completed........")


    def IncreaseDecreaseHadoopNodeSize(self):
        print(" Service available soon!!")

    def Menu(self):
        while True:
            os.system("clear")
            WelcomePage().HypenLine()
            message = "Hadoop Operations"
            print(Colors.FG.green,message.center(WelcomePage.width),Colors.reset)
            WelcomePage().HypenLine()
            print(Colors.FG.orange,"""\n\n Press 1: Create Hadoop Cluster
 Press 2: Hadoop cluster report 
 Press 3: Upload files into cluster
 Press 4: View files
 Press 5: Remove file from cluster
 Press 6: Add new data node
 Press 7: Increase or Decrease data node size
 Press 8: Exit\n\n""",Colors.reset)

            WelcomePage().HypenLine()
            ch = int(input("\n\n Enter your choice: "))
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
                print(Colors.FG.red,"\n Exiting...",Colors.reset)
                exit()
            else:
                print(Colors.FG.red,"\n Invalid choice",Colors.reset)
            con = input("\n\n Do you want to continue? (Y/N): ")
            if con == "Y" or con == "y":
                continue
            else:
                print(Colors.FG.red,"\n Exiting...",Colors.reset)
                exit()

