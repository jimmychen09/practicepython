#http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
import random
import string

chars = []

def password_generator(x):
	for i in range(x):
		chars.append(random.choice(string.ascii_lowercase))
		chars.append(random.choice(string.ascii_uppercase))
		chars.append(random.choice("!@#$%^&*"))
		chars.append(random.choice(string.digits))
		i += 1

def shuffle():
	return random.shuffle(chars)

password_generator(random.randrange(2,4))
shuffle()
password = "".join(chars)

print(password)