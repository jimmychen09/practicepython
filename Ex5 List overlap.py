#http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
import random
import numpy as np

a = np.random.choice(9, random.randint(10,20))
b = np.random.choice(9, random.randint(10,20))

print([x for x in set(a) for y in set(b) if x == y])