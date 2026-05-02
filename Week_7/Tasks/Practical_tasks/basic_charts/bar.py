import random

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(nrows=2, ncols=2)
categories = ['A', 'B', 'C']
values = [10, 25, 15]
data = range(0, 10, random.randint(0, 10))

ax[0, 0].bar(categories, values, color='skyblue')
ax[0, 1].scatter(categories, values, color='pink')
ax[1,0].hist(data, color='#000080')
ax[1, 1].plot(categories, values, color='#800000')

plt.show()