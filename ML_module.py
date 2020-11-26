#!/usr/bin/python3
import os
from WelcomePage import WelcomePage
from Colors import Colors
class ML:
    def SimpleLinearRegression(self):
        filepath = input(" Enter path where code file saved: ")
        if filepath[-1] != "/":
            print(Colors.FG.red,"\n\n Invaild path! Put directory separator at last e.g /a/b/c/",Colors.reset)
            filepath = input(" Enter again: ")
        filename = input(" Enter file name: ")
        os.system(f"docker run --rm -dit --name linearregression -v {filepath}:{filepath} surinder2000/sklearn:v1  python3 {filepath+filename}")

    def MultiLinearRegression(self):
        filepath = input(" Enter path where code file saved: ")
        if filepath[-1] != "/":
            print(Colors.FG.red,"Invalid path! Put directory separator at last e.g /a/b/c/",Colors.reset)
            filepath = input(" Enter again: ")
        filename = input(" Enter file name: ")
        os.system(f"docker run --rm -dit --name linearregression -v {filepath}:{filepath} surinder2000/sklearn:v1  python3 {filepath+filename}")

    def LinearRegression(self):
        while True:
            os.system("clear")
            WelcomePage().HypenLine()
            print(Colors.FG.orange,"""\n\n Press 1: Simple Linear Regression
 Press 2: Multi Linear Regression
 Press 3: Back Menu
 Press 4: Exit\n\n""",Colors.reset)
            WelcomePage().HypenLine()
            ch = int(input("\n\n Enter your choice: "))
            if ch == 1:
                self.SimpleLinearRegression()
            elif ch == 2:
                self.MultiLinearRegression()
            elif ch == 3:
                self.CreateModel()
            elif ch == 4:
                exit()
            else:
                print(Colors.FG.red, "\n\n Invalid Choice",Colors.reset)

            con = input("\n\n Do you want to continue? (Y/N): ")

            if con == "Y" or con == "y":
                continue
            else:
                print(Colors.FG.red,"\n Exiting...",Colors.reset)
                exit()

    def CreateModel(self):
        while True:
            os.system("clear")
            WelcomePage().HypenLine()
            print(Colors.FG.orange, """\n\n Press 1: Linear Regression
 Press 2: Back Menu
 Press 3: Exit\n\n""",Colors.reset)
            WelcomePage().HypenLine()
            ch = int(input("\n\n Enter you choice: "))
            if ch == 1:
                self.LinearRegression()
            elif ch == 2:
                self.Menu()
            elif ch == 3:
                print(Colors.FG.red,"\n Exiting...",Colors.reset)
                exit()
            else:
                print(Colors.FG.red,"\n\n Invalid Choice",Colors.reset)

            con = input("\n\n Do you want to continue? (Y/N): ")

            if con == "Y" or con == "y":
                continue
            else:
                print(Colors.FG.red,"\n Exiting...",Colors.reset)
                exit()


    def Menu(self):
        while True:
            os.system("clear")
            WelcomePage().HypenLine()
            message = "Machine Learning"
            print(Colors.FG.green,message.center(WelcomePage.width),Colors.reset)
            WelcomePage().HypenLine()
            print(Colors.FG.orange,"""\n\n Press 1: Create Model
 Press 2: Exit\n\n""",Colors.reset)
            WelcomePage().HypenLine()
            ch = int(input("\n\n Enter your choice: "))
            if ch == 1:
                self.CreateModel()
            elif ch == 2:
                print(Colors.FG.red,"\n Exiting...",Colors.reset)
                exit()
            else:
                print(Colors.FG.red,"\n\n Invalid Choice",Colors.reset)
            con = input("\n\n Do you want to continue? (Y/N): ")

            if con == "Y" or con == "y":
                continue
            else:
                print(Colors.FG.red,"\n Exiting...",Colors.reset)
                exit()




