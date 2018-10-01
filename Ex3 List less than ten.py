#http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(input("Choose a number: "))
print([i for i in a if i < num])