import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 2, 0.00001)
c = 0.5/0.99
count = 500

f = lambda x: 50 * (x > 0) * (x <= 0.01)   +   c * (x > 0.01) * (x <= 1)
g = lambda x: 50 * np.exp(-4.1 * (x-0.01)) * (x >= 0)
g_inv = lambda x: -0.243902 *  np.log(0.01919658259895598*x)


y1 = f(x)
y2 = g(x)

ran_x = g_inv(np.random.uniform(0, 52, count))
ran_y = np.random.uniform(0, 1, count) * g(ran_x)

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