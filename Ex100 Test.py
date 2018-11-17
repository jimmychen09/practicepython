import random

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('ticks')

# %matplotlib inline

# Create some random data.

x = [random.randrange(10) for n in range(10)]

y = [random.randrange(10) for n in range(10)]

# t = [random.randrange(20) for n in range(15)]

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'magenta']

index = [i for i in range(1, len(colors)+1)]

votes = [3, 2, 5, 1, 7, 0, 2]

# # plt.plot(r, 'm*')

# # plt.plot(s, 'g--')

# # plt.plot(t, 'b-')tick_label='clouds'

plt.bar(index, votes, width=0.75, color=colors, tick_label=colors) 

# plt.pie(x, radius=1)

plt.show()
