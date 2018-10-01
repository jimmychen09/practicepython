#http://www.practicepython.org/exercise/2014/11/11/20-element-search.html
def binarySearch(alist, guess):
	first = 0
	last = len(alist)-1
	while True:
		findMiddle = (first + last)//2
		if guess == alist[findMiddle]:
			print("You found it", alist[findMiddle])
			break
		else:
			if guess > alist[findMiddle]:
				first = findMiddle + 1
			else:
				last = findMiddle - 1

if __name__ == "__main__":
	alist = list(range(0,1000))
	binarySearch(alist, int(input("Enter a guess: ")))