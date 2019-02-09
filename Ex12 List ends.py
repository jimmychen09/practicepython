#http://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
a = [5, 10, 15, 20, 25]

def first_last(a):
	print([i for i in a if i == a[0] or i == a[-1]])

first_last(a)


# bettter example from site: 
# def first_last(a):
# 	return[a[0], a[-1]]