#Challenge 7: Refactoring

def analyze_traffic(addresses, limit):
	blacklist = [i for i in addresses if addresses.count(i) > limit]
	return set(blacklist)

blah = [1,1,1,1,1,1,1,2,2,3,4,4,4,4,5,3,2,7,1,7,2,4,5,6,4,3,2,2,1,7]

print(analyze_traffic(blah, 2))