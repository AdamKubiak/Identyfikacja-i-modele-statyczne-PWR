import numpy as np
from matplotlib import pyplot as plt


amount = 10000
sigma = 2,5
mu = 3
X = np.random.randn(1,amount)
e1 = np.sum(X)/amount
e2 = np.sum(np.power(X-e1,2))
e3 = np.sum(np.power(X-e1,2))/(amount-1)
print(e1)
print(e2)
print(e3)
