import matplotlib.pyplot as plt
import numpy as np

# fig = plt.figure(figsize=[7,6], facecolor='gray')
# x = [9,10,11,12,13,14,15,16]
# y = [235, 237, 232, 235, 233, 232, 237, 235]
# axes = plt.plot(x, y)
#
# plt.title('Stock Apply')
# plt.xlabel('Time in Hours.')
# plt.ylabel('Price')
#
# plt.setp(axes, color='black', linestyle='--', linewidth=2, marker='.', ms=14, mfc='g', mec='black')
# plt.grid()
#
# plt.show()

fig, ax = plt.subplots(figsize=[7,6])

x = np.random.random(6)
y = np.random.random(6)

ax.plot(x, y)
ax.set_title('NASDAQ\nApple Inc.')
ax.set_xlabel('Time in Hours')
ax.set_ylabel('Price $')
plt.show()