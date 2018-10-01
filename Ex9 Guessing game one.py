#http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
import random
num = random.randint(1, 9)
count = 0
print("You may finish the game any time by entering 'exit'")

while True:
	ui = str(input("Enter a number: "))
	if ui == "exit":
		break
	else:
		count += 1
		ui = int(ui)
		if ui > num:
			print("Too high, try again")
		elif ui < num:
			print("Too low, try again")
		else:
			print("You won with", count, "tries!")
			break