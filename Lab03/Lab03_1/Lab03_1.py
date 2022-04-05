import numpy as np
from matplotlib import pyplot as plt


amount = 10000
sigma = 2.5
mu = 3
X = mu + sigma * np.random.randn(1, amount)
e1 = np.sum(X)/amount
e2 = np.sum(np.power(X-e1,2))
e3 = np.sum(np.power(X-e1,2))/(amount-1)
print(e1)
print(e2)
print(e3)

Y = []
for x in range(amount):
    temp = mu + sigma * np.random.randn(1, x)
    y = np.sum(temp) / (x+1)
    Y.append(y)

Y1 = []
for x in range(amount):
    temp = mu + sigma * np.random.randn(1, x)
    e1 = np.sum(temp)/(x+1)
    y = np.sum(np.power(temp-e1,2))
    Y1.append(y)

x = range(amount)
plt.plot(x,Y1)
plt.title("σ = 2.5, μ = 3")
plt.show()
