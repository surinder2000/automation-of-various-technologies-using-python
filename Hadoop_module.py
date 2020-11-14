#!/usr/bin/python3
import os

class Hadoop:
    def ConfigureMaster(self):
        ip = input("Enter host IP: ")
        namenodedir = input("Enter namenode directory name: ")



    def ConfigureSlaves(self):
        pass

    def OnLocalSystem(self):
        while True:
            print("""Press 1: Configure Master
Press 2: Confiure Slaves
Press 3: Back Menu
Press 4: Exit""")

            ch = int(input("Enter your choice: "))
            if ch == 1:
                self.ConfigureMaster()
            elif ch == 2: 
                self.ConfigureSlaves()
            elif ch == 3:
                self.OnLocalSystem()
            elif ch == 4:
                exit()
            else:
                print("Invalid choice")
            con = input("Do you want to continue? (Y/N): ")

            if con == "Y" or con == "y":
                continue
            else:
                break

    
    def OnAWSCloud(self):
        pass

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
            os.system("tput setaf 5")
            print("\n----------------Hadoop Management---------------\n")
            print("""Press 1: Create Hadoop Cluster
Press 2: Upload files into cluster
Press 3: View files
Press 4: Remove file from cluster
Press 5: Add new data node
Press 6: Increase or Decrease data node size
Press 7: Back Menu
Press 8: Exit""")

            ch = int(input("Enter your choice: "))
            if ch == 1:
                self.CreateHadoopCluster()
            elif ch == 2:
                self.UploadFiles()
            elif ch == 3:
                self.ViewFiles()
            elif ch == 4:
                self.RemoveFile()
            elif ch == 5:
                self.AddNewNode()
            elif ch == 6:
                self.IncreaseDecreaseNodeSize()
            elif ch == 7:
                print("Baack menu")
            elif ch == 8:
                exit()
            else:
                print("Invalid choice")
                ch = int(input("Enter your choice: "))

            con = input("Do you want to continue? (Y/N): ")
            if con == "Y" or con == "y":
                continue
            else:
                break

h = Hadoop()
h.Menu()

