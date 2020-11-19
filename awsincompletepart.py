#AWS CLOUD FRONT Menu
def awscf():
	os.system('clear')
	while True:
		os.system("clear")
		print("""\n ------- AWS Cloud Front Menu -------
Press 1 : To create New Key
Press 2 : To list the available Keys
Press 3 : To delete any Key
			""")
		print('\n')
		choice=input("Enter Your Choice : ")

		if ("exit" in choice) or ("back" in choice):
			break
		elif choice=="1":
			print("\n------- New Instance Creation -------\n")
		elif choice=="2":
			print(2)
		elif choice=="3":
			print(3)
		elif choice=="4":
			print(4)
		elif choice=="5":
			print(5)
		
		else:
			print("Invalid Choice. Try Again!")

		input("\n\nPress Enter to continue..")
#AWS CLOUD FRONT Menu ENDS

#AWS IAM Menu
def awsiam():
	os.system('clear')
	while True:
		os.system("clear")
		print("""\n ------- IAM USER Management  -------

Press 1 : To list existing IAM Users
Press 2 : To Create new IAM User
Press 3 : To delete any Key

Note : Only possible if the Logged In user has this power

			""")
		print('\n')
		choice=input("Enter Your Choice : ")

		if ("exit" in choice) or ("back" in choice):
			break
		elif choice=="1":
			os.system("aws iam list-users --output text")
		elif choice=="2":
			print(2)
		elif choice=="3":
			print(3)
		elif choice=="4":
			print(4)
		elif choice=="5":
			print(5)
		
		else:
			print("Invalid Choice. Try Again!")

		input("\n\nPress Enter to continue..")
#AWS IAM Menu ENDS

