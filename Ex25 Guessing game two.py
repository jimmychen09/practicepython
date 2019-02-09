#http://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html
'''
Game 1 with binary
'''
print("Guess a number between 0 and 100")
first = 0
last = 101
counter = 0
guesses = []
while True:
	middle = (first + last)//2
	print("Is it...", middle, "?")
	inp = input("Is it higher, lower or correct? ")
	counter += 1
	guesses.append(middle)
	if inp == "higher":
		first = middle
	elif inp == "lower":
		last = middle
	else:
		break
print("So the number is", middle, "and I took", counter, "guesses. They were", guesses)

'''
Game 2 with random
'''
# import random

# print("Guess a number between 0 and 100")
# first = 0
# last = 100
# counter = 0
# guesses = []
# while True:
# 	guess = random.randint(first, last)
# 	print("Is it...", guess, "?")
# 	inp = input("Is it higher, lower or correct? ")
# 	counter += 1
# 	guesses.append(guess)
# 	if inp == "higher":
# 		first = guess + 1
# 	elif inp == "lower":
# 		last = guess - 1
# 	else:
# 		break
# print("So the number is", guess, "and I took", counter, "guesses. They were", guesses)