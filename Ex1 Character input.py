#http://www.practicepython.org/exercise/2014/01/29/01-character-input.html
import datetime

get = datetime.datetime.now()
d = {"NAME": 0, "YEAR": 0}
d["NAME"] = str(input("Enter your name: "))
d["YEAR"] = get.year + (100 - int(input("Enter your age: ")))
copy = int(input("How many times should I repeat this? " ))
print(copy * ("Hello %s. You will be 100 years old in year %r. \n" %(d["NAME"], d["YEAR"])))