#http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
word = input("Enter a word: ")
reverse_word = word[::-1]

if str.lower(word).replace(" ","") == str.lower(reverse_word).replace(" ",""):
	print(word, "is a palindrome")
else:
	print(word, "is not a palindrome")