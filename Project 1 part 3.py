#Challenge 3: Building a New List

messages = ["This is a message.", "So is this.",
"The quick brown fox jumped over the lazy dog. Then the fox did it again."]
more_than_forty_chars = []

for i in messages:
	if len(i) > 40:
		more_than_forty_chars.append(i)

print(i)