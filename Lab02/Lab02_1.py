import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-1, 1, 0.000005)
c = 2
count = 10000

f = lambda x: (x + 1) * (x > -1) * (x <= 0)   +   (-x + 1) * (x > 0) * (x <= 1)
g = lambda x: c * 0.5 * np.exp(-np.abs(x))
g_inv = lambda x:  np.log(2*x) * (x <= 1/2) - np.log(-2*x + 2) * (x > 1/2)

y1 = f(x)
y2 = g(x)

plt.show()
