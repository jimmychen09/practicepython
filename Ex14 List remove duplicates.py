#http://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []

def remove_dup(a, b):
	for x in a:
		for y in b:
			if x == y:
				if x not in c:
					c.append(x)

remove_dup(a, b)
print(c)