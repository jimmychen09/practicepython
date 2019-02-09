#http://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html
import os
import sys

def clear_screen():
    if sys.platform  == 'win32':
        clear = 'cls'
    else:
        clear = 'clear'
    return clear

def display_game(game):
	os.system(clear_screen())
	d = {0:' ', 1:'X', 2:'O'}
	print("Enter row, comma and column for your move\n(eg 1,1 is the top row, left column)")
	for x in range(0, 3):
		print(' ---' * 3)
		new_row = []
		for y in range(0, 3):
			new_row.append(d[game[x][y]])
		print(''.join(str(new_row).replace('[','| ').replace(']',' |').replace(',', ' |').replace("'",'')))
	print(' ---' * 3)

def check_win(game):
	for i in range(0,3):
		horizontal = set([game[i][0], game[i][1], game[i][2]])
		vertical = set([game[0][i], game[1][i], game[2][i]])
		if len(horizontal) == 1 and horizontal != 0:
			return game[i][0]
		if len(vertical) == 1 and vertical != 0:
			return game[0][i]
	 
	diagonal1 = set([game[0][0], game[1][1], game[2][2]])
	diagonal2 = set([game[0][2], game[1][1], game[2][0]])
	if len(diagonal1) == 1 or len(diagonal2) == 1 and game[1][1] != 0:
		return game[1][1]
	return 0

def plays(player):
	while True:
		inp = input("Player " + str(player) + ", make your move: ")
		pos = [x.strip() for x in inp.split(',')]
		x, y = pos
		if game[int(x)-1][int(y)-1] == 0:
			game[int(x)-1][int(y)-1] = player
			break
		else:
			print("Spot already taken. Choose again.")

def moves_left(game):
	if any(0 in x for x in game):
		return True
	else:
		return False

def switch_players(player):
	if player == 1:
		return 2
	elif player == 2:
		return 1

if __name__ == "__main__":
	game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
	winner = 0
	player = 1
	while winner == 0 and moves_left(game):
		display_game(game)
		plays(player)
		if check_win(game) == player:
			display_game(game)
			print("Player", player, "Wins!")
			winner = player
			break
		if moves_left(game) == False:
			display_game(game)
			print("End game. Draw.")
		player = switch_players(player)