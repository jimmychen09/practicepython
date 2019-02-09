#http://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html
import random

rand_num = ''.join(random.sample("0123456789", 4))

print("Welcome to the Cows and Bulls Game!\nYou may exit the game anytime by typing exit")

def cows_bulls(a, b):
	global count_cows, count_bulls
	count_cows = 0
	count_bulls = 0
	for i in range(len(user_num)):
		if a[i] == b[i]:
			count_cows += 1
		elif a[i] != b[i] and a[i] in b:
			count_bulls += 1
		else:
			pass

if __name__ == "__main__":
	guess = 0
	while True:
		user_num = str(input("Enter a 4 digit number: "))
		guess += 1
		if user_num == rand_num:
			print("Congratulations. You correctly guessed", rand_num, "with", guess, "guesses!")
			break
		elif user_num == "exit":
			break
		else:
			cows_bulls(user_num, rand_num)
			print(count_cows, "cows,", count_bulls, "bulls")
			pass