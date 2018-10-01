#http://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html
def CheckWinner(game):
	for x in range(0,3):
		horizontal = set([game[x][0], game[x][1], game[x][2]])
		if len(horizontal) == 1 and horizontal != 0:
			return game[x][0]
	for y in range(0,3):
		vertical = set([game[0][y], game[1][y], game[2][y]])
		if len(vertical) == 1 and vertical != 0:
			return game[0][y]
	 
		diagonal1 = set([game[0][0], game[1][1], game[2][2]])
		diagonal2 = set([game[0][2], game[1][1], game[2][0]])
		if len(diagonal1) == 1 or len(diagonal2) == 1 and game[1][1] != 0:
			return game[1][1]

	return 0

winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

print(CheckWinner(winner_is_also_1))