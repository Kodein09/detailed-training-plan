import numpy as np
from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt

ws = [3, 2, 3]
hs = [2, 1]

fig = plt.figure(figsize=(7, 5))
gs = GridSpec(ncols=3, nrows=2, figure=fig, width_ratios=ws, height_ratios=hs)

ax1 = plt.subplot(gs[0, 0])
ax1.plot(np.arange(0, 5, 0.2))

ax2 = fig.add_subplot(gs[1, 0:2])
ax2.plot(np.random.random(10))

ax3 = plt.subplot(gs[:, 2])
ax3.plot(np.random.random(10))

plt.show()