from WelcomePage import WelcomePage
from Colors import Colors
from ML_module import ML
from Hadoop_module import Hadoop
from Docker import Container
from AWS import AWS
import os
def MainMenu():
    os.system('clear')
    WelcomePage().PrintHeader()
    while True:
        os.system('clear')
        WelcomePage().HypenLine()
        message = "On which technology do you want to work"
        print(Colors.FG.green,message.center(WelcomePage.width),Colors.reset)
        WelcomePage().HypenLine()
        print(Colors.FG.orange,"""\n\n Press 1: Hadoop
 Press 2: AWS Cloud
 Press 3: Docker
 Press 4: Machine Learning
 Press 5: Exit\n\n""",Colors.reset)
        WelcomePage().HypenLine()
        ch = int(input("\n\n Enter your choice: "))
    
        if ch == 1:
            Hadoop().Menu()
        elif ch == 2:
            AWS().Menu()
        elif ch == 3:
            Container().DockerMenu()
        elif ch == 4:
            ML().Menu()
        elif ch == 5:
            print(Colors.FG.red,"\nExiting...",Colors.reset)
            exit()
        else:
            print(Colors.FG.red,"Invaild choice",Colors.reset)

        con = input("\n\n Do you want to continue main? (Y/N): ")

        if con == "y" or con == "Y":
            continue
        else:
            print(Colors.FG.red,"\nExiting...",Colors.reset)
            exit()



MainMenu()
