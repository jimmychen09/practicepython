#http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
ui = int(input(("Enter a number: ")))

def divisors(num):
	return[i for i in range(1, num + 1) if num % i == 0]

def is_prime(ui):
	if len(divisors(ui)) == 2:
		print(ui, "is prime number")
	else:
		print(ui, "is not prime number")

is_prime(ui)