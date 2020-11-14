#!/usr/bin/python3
import os

class ML:
    def LinearRegression(self):
        os.system("clear")
        print("""Press 1: Simple Linear Regression
Press 2: Multi Linear Regression
Press 3: Back Menu
Press 4: Exit""")
        ch = int(input())
        if ch == 1:
            self.SimpleLinearRegression()
        elif ch == 2:
            self.MuliLinearRegression()
        elif ch == 3:
            self.CreateModel()
        elif ch == 4:
            exit()
        else:
            print("Invalid Choice")

    def CreateModel(self):
        os.system("clear")
        print("""Press 1: Linear Regression
Press 2: Back Menu
Press 3: Exit""")
        ch = int(input())
        if ch == 1:
            self.LinearRegression()
        elif ch == 2:
            self.Menu()
        elif ch == 3:
            exit()
        else:
            print("Invalid Choice")


    def Menu(self):
        os.system("clear")
        os.system("tput setaf 5")
        print("\n-----------------Machine Learning------------------\n")
        print("""Press 1: Create Model
Press 2: Exit""")
        ch = int(input())
        if ch == 1:
            self.CreateModel()
        elif ch == 2:
            exit()
        else:
            print("Invalid Choice")


ml = ML()
ml.Menu()


