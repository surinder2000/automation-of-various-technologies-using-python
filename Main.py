from WelcomePage import WelcomePage
from Colors import Colors
from ML_module import ML
from Hadoop_module import Hadoop
from Docker import Container
import os
def MainMenu():
    while True:
        os.system('clear')
        WelcomePage().PrintHeader()
        os.system('clear')
        WelcomePage().HypenLine()
        message = "On which technology do you want to work"
        print(Colors.FG.green,message.center(WelcomePage.width),Colors.reset)
        WelcomePage().HypenLine()
        print("\n\n")
        print("""Press 1: Hadoop
Press 2: AWS Cloud
Press 3: Docker
Press 4: Machine Learning
Press 5: Exit""")

        ch = int(input("Enter your choice: "))
    
        if ch == 1:
            Hadoop().Menu()
        elif ch == 2:
            pass
        elif ch == 3:
            Container().DockerMenu()
        elif ch == 4:
            ML().Menu()
        elif ch == 5:
            exit()
        else:
            print("Invaild choice")

        con = input("Do you want to continue main? (Y/N): ")

        if con == "y" or con == "Y":
            continue
        else:
            exit("Exiting....")



MainMenu()
