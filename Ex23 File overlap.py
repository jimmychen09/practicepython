#http://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html
with open('primenumbers.txt', 'r') as f:
	prime = []
	for line in f:
		line = line.strip()
		prime.append(int(line))

with open('happynumbers.txt', 'r') as f:
	happynumbers = []
	for line in f:
		line = line.strip()
		happynumbers.append(int(line))

print("prime", prime)
print("happy", happynumbers)
print("both", [x for x in prime for y in happynumbers if x == y])