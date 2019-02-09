#Challenge 2: Checking a List of Messages

messages = ["This is a message.", "So is this.",
"The quick brown fox jumped over the lazy dog. Then the fox did it again."]

for i in messages:
	if len(i) > 40:
		print(i, "More than 40 characters!")