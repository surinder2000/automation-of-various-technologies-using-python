#!/usr/bin/python3
import os

class ML:
    def SimpleLinearRegression(self):
        filepath = input("Enter path where code file saved: ")
        if filepath[-1] != "/":
            print("Invaild path! Put directory separator at last e.g /a/b/c/")
            filepath = input("Enter again: ")
        filename = input("Enter file name: ")
        os.system(f"docker run --rm -dit --name linearregression -v {filepath}:{filepath} surinder2000/sklearn:v1  python3 {filepath+filename}")
    def MultiLinearRegression(self):
        filepath = input("Enter path where code file saved: ")
        if filepath[-1] != "/":
            print("Invalid path! Put directory separator at last e.g /a/b/c/")
            filepath = input("Enter again: ")
        filename = input("Enter file name: ")
        os.system(f"docker run --rm -dit --name linearregression -v {filepath}:{filepath} surinder2000/sklearn:v1  python3 {filepath+filename}")

    def LinearRegression(self):
        while True:
            os.system("clear")
            print("""Press 1: Simple Linear Regression
Press 2: Multi Linear Regression
Press 3: Back Menu
Press 4: Exit""")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                self.SimpleLinearRegression()
            elif ch == 2:
                self.MultiLinearRegression()
            elif ch == 3:
                self.CreateModel()
            elif ch == 4:
                exit()
            else:
                print("Invalid Choice")

            con = input("Do you want to continue? (Y/N): ")

            if con == "Y" or con == "y":
                continue
            else:
                exit()

    def CreateModel(self):
        while True:
            os.system("clear")
            print("""Press 1: Linear Regression
Press 2: Back Menu
Press 3: Exit""")
            ch = int(input("Enter you choice: "))
            if ch == 1:
                self.LinearRegression()
            elif ch == 2:
                self.Menu()
            elif ch == 3:
                exit()
            else:
                print("Invalid Choice")

            con = input("Do you want to continue? (Y/N): ")

            if con == "Y" or con == "y":
                continue
            else:
                exit()


    def Menu(self):
        while True:
            os.system("clear")
            print("\n-----------------Machine Learning------------------\n")
            print("""Press 1: Create Model
Press 2: Exit""")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                self.CreateModel()
            elif ch == 2:
                exit()
            else:
                print("Invalid Choice")
            con = input("Do you want to continue? (Y/N): ")

            if con == "Y" or con == "y":
                continue
            else:
                exit()




