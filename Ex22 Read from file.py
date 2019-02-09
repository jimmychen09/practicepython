# http://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html
from collections import Counter

def find_between(s, first, last):
    try:
        start = s.index(first) + 3
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""

with open('nameslist.txt', 'r') as open_file:
	categoryDict = {}
	for line in open_file:
		line = line.strip()
		if line in categoryDict:
			categoryDict[line] += 1
		else:
			categoryDict[line] = 1
print(categoryDict)

with open('Training_01.txt', 'r') as open_file:
	categoryDict = {}
	for line in open_file:
		line = find_between(line, "/", "/sun_")
		if line in categoryDict:
			categoryDict[line] += 1
		else:
			categoryDict[line] = 1
print(categoryDict)