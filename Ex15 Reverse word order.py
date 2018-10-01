#ttp://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
def reverse_word(i):
	result = input(i).split()
	result = " ".join(result[::-1])
	print(result)

reverse_word("Enter a sentence: ")