import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-1, 1, 0.00001)
r = 1
c = 1
count = 10000

f = lambda x: np.sqrt(np.power(r, 2) - np.power(x, 2))
g = lambda x: c * (x >= -1) * (x <= 1)

y1 = f(x)
y2 = g(x)

ran_x = np.random.uniform(-1, 1, count)
ran_y = np.random.uniform(0, g(ran_x), count)
good_x = []
good_y = []
bad_x = []
bad_y = []

for i in range(ran_x.size):
  if ran_y[i] <= f(ran_x[i]):
    good_x.append(ran_x[i])
    good_y.append(ran_y[i])
  else:
    bad_x.append(ran_x[i])
    bad_y.append(ran_y[i])



fig, (ax) = plt.subplots(1, 2)

ax[1].plot(x, y1, label='f(x)')
ax[1].plot(x, y2, label='cg(x)')
ax[1].plot(good_x, good_y, 'o',color='blue')
ax[1].plot(bad_x, bad_y, 'o',color='orange')
ax[1].set_ylabel('Y')
ax[1].set_xlabel('X')
ax[1].legend()

ax[0].hist(good_x, density=True, label="Histogram", bins=100)
ax[0].set_xlabel('Wartość próbki')
ax[0].set_ylabel('Ilość próbek o danej wartości')

plt.show()