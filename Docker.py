import os
import sys
from Colors import Colors
from WelcomePage import WelcomePage
class Container:
    def DockerMenu(self):
        while True:
            os.system('clear')
            WelcomePage().HypenLine()
            greet = "Welcome to Docker assistant!"
            print(Colors.FG.green, greet.center(WelcomePage.width),Colors.reset)
            WelcomePage().HypenLine()
            print("""Press 1: To start docker engine
Press 2: To stop docker engine
Press 3: To list docker info
Press 4: To list all docker os
Press 5: To launch docker OS
Press 6: To start docker OS
Press 7: To attach screen to docker OS
Press 8: To delete docker OS
Press 9: To delete All docker OS
Press 10: To download docker image
Press 11: To remove docker image
Press exit: To go back to Main Menu
Press quit or close: To quit the program \n""")
            choiceDocker = input('Enter your choice: ')

            if choiceDocker == '1' :
                os.system('systemctl start docker')
            elif choiceDocker == '2' :
                os.system('systemctl stop docker')
            elif choiceDocker == '3' :
                os.system('docker info')
            elif choiceDocker == '4' :
                os.system('docker ps -a')
            elif choiceDocker == '5' :
                imageName = input("Enter OS Image: ")
                imageVersion = input("Enter image version: ")
                OSName = input("Enter name tag: ")
                launchInfo = 'docker run -dit --name ' + OSName + '  ' + imageName + ':' + imageVersion
                os.system(launchInfo)
            elif choiceDocker == '6' :
                OSName = input("Enter OS name: ")
                startInfo = 'docker start ' + OSName
                os.system(startInfo)
            elif choiceDocker == '7' :
                OSName = input("Enter OS name: ")
                attachInfo = 'docker attach ' + OSName
                os.system(attachInfo)
            elif choiceDocker == '8' :
                OSName = input("Enter OS name: ")
                deleteInfo = 'docker rm -f ' + OSName
                os.system(deleteInfo)
            elif choiceDocker == '9' :
                os.system('docker rm -f `docker ps -a -q`')
            elif choiceDocker == '10' :
                imageName = input("Enter image os: ")
                imageVersion = input("Enter image version: ")
                pullInfo = 'docker pull ' + imageName + ':' + imageVersion
                os.system(pullInfo)
            elif choiceDocker == '11' :
                imageName = input("Enter image os : ")
                imageVersion = input("Enter OS version : ")
                removeInfo = 'docker rmi -f ' + imageName + ':' + imageVersion
                os.system(removeInfo)
            elif choiceDocker == 'exit' :
                break
            elif (choiceDocker == "quit") or (choiceDocker == "close") :
                sys.exit("Exiting..")
            else :
                print(Colors.FG.red,"Error: Wrong Input!",Colors.reset)
            vague_cnf = input("Press Enter to continue...")

dock = Container()
dock.DockerMenu()
