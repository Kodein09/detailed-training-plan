# import matplotlib.pyplot as plt
#
# # fig, ax = plt.subplots()
#
# fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1)
# ax1.plot([1, 2, 3], [10, 20, 30]) #Ось абсцисс (x) - [1,2,3], Ось ординат (y) = [10, 20, 30]
# ax2.plot([4,5,6], [40, 50, 60]) #Ось абсцисс (x) - [4,5,6], Ось ординат (y) = [40, 50, 60]
# ax3.plot([1, 5, 15], [0, 15, 30])
# ax1.set_title('Динамика выручки')
# ax2.set_title('Динамика продаж')
# ax3.set_title('Количество клиентов')
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
#
# fig, ax = plt.subplots()
# ax.plot([1,2,3,4], [1,2,3,4])
# plt.show()

# import matplotlib.pyplot as plt
# from matplotlib.ticker import NullLocator, NullFormatter, Locator, LinearLocator, MultipleLocator, FixedLocator
# import numpy as np
#
# fig = plt.figure(figsize=(7, 5))
# ax = fig.add_subplot()
# ax.plot(np.arange(start=0, stop=8, step=0.5))
# ax.set(xlim=[0, 15], ylim=[0, 10])
# x = np.arange(-np.pi/2, np.pi, 0.1)

#major
# ax.xaxis.set_major_locator(MultipleLocator(base=1))
# ax.yaxis.set_major_locator(MultipleLocator(base=1))
# ax.xaxis.set_major_locator(FixedLocator([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]))
# ax.yaxis.set_major_locator(FixedLocator([0, 1, 2, 3, 4, 5]))

#minor
# ax.xaxis.set_minor_locator(NullLocator())
# plt.grid()
# plt.show()


# ax.set(xlim=[-5, 30], ylim=[-1, 10])
# ax.set_xlim(xmin=-5, xmax=15)
# ax.set_ylim(ymin=-2, ymax=10)
# plt.xlim(-1, 15)
# plt.ylim(-2, 12)


from matplotlib.ticker import NullFormatter, FormatStrFormatter, FuncFormatter, ScalarFormatter, FixedFormatter
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams["axes.formatter.limits"] = (-4, 4)

def tick_repr(num: int, pos) -> str:
    return f"[{num}]" if num < 0 else f"({num})"

fig = plt.figure(figsize=(7, 5))
x = np.arange(-np.pi/2, np.pi, 0.1)
ax = fig.add_subplot()
ax.plot(x, np.sin(x) * 1e5)
# ax.xaxis.set_major_formatter(NullFormatter())
# ax.yaxis.set_major_formatter(NullFormatter())

# ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
# ax.yaxis.set_major_formatter(FormatStrFormatter('%'))
# ax.xaxis.set_major_formatter(FuncFormatter(tick_repr))

# sf = ScalarFormatter()
# sf.set_powerlimits((-6, 6))
# ax.yaxis.set_major_formatter(sf)
plt.grid()
plt.show()

import matplotlib.pyplot as plt
from scipy.stats import norm, gaussian_kde

x = np.linspace(-4, 4, 100)
y = norm.pdf(x, loc=0, scale=1)

fig = plt.figure(figsize=(7, 5))

# plt.hist(randn, bins=30, edgecolor='black')
# plt.plot(x, y, color='blue', linewidth=2)
# plt.title("Frequency Gaussian distribution/bell curve.")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.grid()

ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(x, y)
ax1.set(xlabel='Value', ylabel='Frequency')
ax1.grid()

ax2 = fig.add_subplot(2, 2, 2)
ax2.bar(x, y, color='maroon')
ax2.set(xlabel='Value', ylabel='Frequency')
ax2.grid()

ax3 = fig.add_subplot(2, 2, 3)
ax3.hist(randn, bins=30, color='blue')
ax3.set(xlabel='Value', ylabel='Frequency')
ax3.grid()

ax4 = fig.add_subplot(2, 2, 4)
ax4.scatter(x, y, color='green')
ax4.set(xlabel='Value', ylabel='Frequency')
ax4.grid()

plt.show()

data = np.random.randn(100000)

density = gaussian_kde(data)
x = np.linspace(min(data), max(data), 100)
y = density(x)

# plt.hist(data, color='gray', bins=30, density=True, alpha=0.6, label="гистограмма данных")
plt.fill_between(x, y, color='gray', alpha=0.6)
plt.plot(x, y, color='red', linewidth=2, label="Кривая через plt.plot()")

plt.title("Частотный график: Совмещение гистограммы и линии")
plt.xlabel("Значение (Value)")
plt.ylabel("Плотность частоты (Density)")

plt.legend()
plt.grid()
plt.show()