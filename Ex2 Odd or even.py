#http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
num = int(input("Enter a number: "))
check = int(input("Enter a number to divide by: "))

if num % 2 == 1:
	print(num, "is odd")
elif num % 4 == 0:
	print(num, "is even and a multiple of 4")
else:
	print (num, "is even")

if num % check == 0:
	print(num, "divides evenly into", check)
else:
	print(num, "does not divide evenly into", check)