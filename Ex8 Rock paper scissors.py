#http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
import getpass
options = ["Rock", "Paper", "Scissor"]

while True:
	try:
		value1 = getpass.getpass("Person 1; Enter Rock, Paper or Scissor: ")
		if value1 not in options:
			print("You made an incorrect selection. Please select Rock, Paper or Scissor")
			continue
		value2 = getpass.getpass("Person 2; Enter Rock, Paper or Scissor: ")
		if value2 not in options:
			print("You made an incorrect selection. Please select Rock, Paper or Scissor")
			continue
		retry = False
		if value1 == value2:
			retry = True
			print("You both picked", value1, "\nGo again")
		elif (value1 == "Rock" and value2 == "Scissor") or (value1 == "Paper" and value2 == "Rock") or (value1 == "Scissor" and value2 == "Paper"):
			print("Person 1 entered", value1,"\nPerson 2 entered", value2, "\nWinner is Person 1")
		else:
			print("Person 1 entered", value1,"\nPerson 2 entered", value2, "\nWinner is Person 2")
		if retry == False:
			user_input = input("Do you want to play again? (y/n): ")
			if user_input != "y":
				break
	except:
		break