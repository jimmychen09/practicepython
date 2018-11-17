#Challenge 5: Checking a List of Messages

message1 = ["This is a message.", "So is this.",
"The quick brown fox jumped over the lazy dog. Then the fox did it again.",
"This is a message.", "So is this.",
"The quick brown fox jumped over the lazy dog. Then the fox did it again.",
"This is a message.", "So is this.",
"The quick brown fox jumped over the lazy dog. Then the fox did it again.",
"This is a message.", "So is this.",
"The quick brown fox jumped over the lazy dog. Then the fox did it again."]
message2 = ["In the last set of challenges", 
"you wrote some code to take a list of strings",
"and create a new list from it called ",
"In the last set of challenges", 
"you wrote some code to take a list of strings",
"and create a new list from it called "]
message3 = ["Your mission this time", "should you choose to accept it", "is to",
"Your mission this time", "should you choose to accept it", "is to"]

def get_unique_over_forty_chars(messages):
	more_than_forty_chars = {}
	bucket = []
	occurrence_cnt = 0
	for i in messages:
		bucket.append(i)
		occurrence_cnt = bucket.count(i)
		if len(i) > 40:
			more_than_forty_chars[i] = occurrence_cnt
	return more_than_forty_chars.keys()

print("message1", get_unique_over_forty_chars(message1))
print("message2", get_unique_over_forty_chars(message2))
print("message3", get_unique_over_forty_chars(message3))