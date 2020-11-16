import os
class colors: 
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg: 
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg: 
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

rows, columns = os.popen('stty size', 'r').read().split()
width = int(columns)

os.system('clear')

hashLine = '#'
print(colors.fg.pink,end="")
print(hashLine.center(width,'#'),colors.reset)
print('\n\n\n\n\n\n')

print(colors.fg.red, colors.bold,'\t\t\t\t\t\t\t\t\t\tA',end="")
print(colors.reset,end="")
print("rth\n\n")
print("\t\t\t\t\t\t\t\t\t     Team Task\n\n")
print(colors.fg.lightcyan,"\t\t\t\t\t\t   'Menu based Python program integrating all learnt technologies'",colors.reset)
print("\n\n")

welcomeLine = 'Welcome!!'
print(welcomeLine.center(width))

print(colors.fg.lightgrey,end="")
continueLine = "Press enter to Continue..."
print(continueLine.center(width),colors.reset)

print('\n\n\n\n\n\n')
print(colors.fg.pink,end="")
print(hashLine.center(width,'#'),colors.reset)
input()


