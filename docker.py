import os
import sys
class container:
    def docker() :
        while True:
            os.system('clear')
            hash()
            greet = "Welcome to Docker assistant!"
            print(colors.fg.green)
            print(greet.center(width))
            print(colors.reset)
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
            choiceDocker = input('Enter your choice : ')

            if choiceDocker == '1' :
                os.system('systemctl start docker')
            elif choiceDocker == '2' :
                os.system('systemctl stop docker')
            elif choiceDocker == '3' :
                os.system('docker info')
            elif choiceDocker == '4' :
                os.system('docker ps -a')
            elif choiceDocker == '5' :
                osName = input("Enter image os : ")
                osVersion = input("Enter OS version : ")
                launchInfo = 'docker run -it ' + osName + ':' + osVersion
                os.system(launchInfo)
            elif choiceDocker == '6' :
                osName = input("Enter os name: ")
                startInfo = 'docker start ' + osName
                os.system(startInfo)
            elif choiceDocker == '7' :
                osName = input("Enter os name: ")
                attachInfo = 'docker attach ' + osName
                os.system(attachInfo)
            elif choiceDocker == '8' :
                osName = input("Enter os name: ")
                deleteInfo = 'docker rm -f ' + osName
                os.system(deleteInfo)
            elif choiceDocker == '9' :
                os.system('docker rm `docker ps -a -q`')
            elif choiceDocker == '10' :
                osName = input("Enter image os : ")
                osVersion = input("Enter OS version : ")
                pullInfo = 'docker pull ' + osName + ':' + osVersion
                os.system(pullInfo)
            elif choiceDocker == '11' :
                osName = input("Enter image os : ")
                osVersion = input("Enter OS version : ")
                removeInfo = 'docker rmi -f ' + osName + ':' + osVersion
                os.system(removeInfo)
            elif choiceDocker == 'exit' :
                break
            elif (choiceDocker == "quit") or (choiceDocker == "close") :
                sys.exit("Exiting..")
            else :
                print(colors.fg.red,"Error: Wrong Input!",colors.reset)
            vague_cnf=input("\n\n Press Enter to continue...")

dock=container()
dock.docker()