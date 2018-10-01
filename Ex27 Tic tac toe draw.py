#http://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html
game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

print("Enter row, comma and column for your move (eg 1,1 for top row, left column)")

while True:
	if any(0 in x for x in game):
		print(game)
		inp = input("Player 1, your move: ")
		move = [x.strip() for x in inp.split(',')]
		x, y = move
		if game[int(x)-1][int(y)-1] == 0:
			game[int(x)-1][int(y)-1] = "X"
		else:
			print("Place your X in a spot not already taken")
	else:
		print("End game")
		break

	if any(0 in x for x in game):
		print(game)
		inp = input("Player 2, your move: ")
		move = [x.strip() for x in inp.split(',')]
		x, y = move
		if game[int(x)-1][int(y)-1] == 0:
			game[int(x)-1][int(y)-1] = "O"
		else:
			print("Place your O in a spot not already taken")
	else:
		print("End game")
		break