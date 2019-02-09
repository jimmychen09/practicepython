#http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
ui = int(input("How many Fibonacci numbers to generate? "))

num1= 0
num2 = 1
num3 = 0
seq = []
count = 0

while count < ui:
	count += 1
	num1 = num2
	num2 = num3
	num3 = num1 + num2
	seq.append(num3)

print(seq)