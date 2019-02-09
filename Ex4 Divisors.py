#http://www.practicepython.org/exercise/2014/02/26/04-divisors.html
num = int(input("Enter a number: "))
print([i for i in range(1, num + 1) if num % i == 0])

# l = []
# for i in range(1, num + 1):
# 	if num % i == 0:
# 		l.append(i)
# print(l)