#Challenge 6: Traffic Analysis?
def analyze_traffic(addresses, limit):
	traffic = {}
	blacklist = []
	for address in addresses:
		if address not in traffic:
			traffic[address] = 1
		else:
			traffic[address] += 1
		if traffic[address] > limit:
			if address not in blacklist:
				blacklist.append(address)
	return blacklist

connections = [1,1,1,1,1,1,1,2,2,3,4,4,4,4,5,3,2,7,1,7,2,4,5,6,4,3,2,2,1,7]

print(analyze_traffic(connections, 2))