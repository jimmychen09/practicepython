#http://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html
def board(rows, columns):
	for i in range(0, rows):
		print(" ---" * columns)
		print("|   " * (columns + 1))
	print(" ---" * columns)

rows = int(input("how many rows?"))
columns = int(input("how many columns?"))
board(rows, columns)