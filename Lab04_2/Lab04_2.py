import numpy as np
from matplotlib import pyplot as plt

count = 1000000

mu = 0
sigma = 5
L = 100

T = sigma * np.random.randn(L, count) + mu

estimator1 = np.sum(T, -1) / count
estimator1_2 = np.reshape(estimator1, (L, 1))

estimator2 = np.sum(np.power(T - estimator1_2, 2), -1) / count
estimator3 = np.sum(np.power(T - estimator1_2, 2), -1) / (count - 1)

err1 = np.sum(np.power(estimator1 - mu, 2)) / L
err2 = np.sum(np.power(estimator2 - sigma**2, 2)) / L
err3 = np.sum(np.power(estimator3 - sigma**2, 2)) / L

print(err1)
print(err2)
print(err3)