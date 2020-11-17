from Colors import Colors
import os
os.system("clear")
class WelcomePage:
    rows, columns = os.popen('stty size', 'r').read().split()
    width = int(columns)
    def HypenLine(self):
        hashsymbol = '-'
        print(Colors.FG.pink,hashsymbol.center(self.width-2,'-'),Colors.reset)

    def PrintHeader(self):
        self.HypenLine()
        print('\n\n')
        text1 = "ARTH"
        print(Colors.FG.red, Colors.bold, text1.center(self.width-6),Colors.reset)
        print("\n\n")
        text2 = "Team Task"
        print(text2.center(self.width))
        print("\n\n")
        title = "Menu based program for integrating various technologies"
        print(Colors.FG.lightcyan,title.center(self.width),Colors.reset)
        print("\n\n")
        welcomeLine = 'Welcome!!'
        print(welcomeLine.center(self.width),Colors.FG.lightgrey)
        print("Press enter to Continue...")
        self.HypenLine()
        input()

