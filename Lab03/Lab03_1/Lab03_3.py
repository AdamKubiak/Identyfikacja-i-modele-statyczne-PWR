
import numpy
import numpy as np
import matplotlib.pyplot as plt
u = 0 # expected value
o = 2 # variance value
size = 10000
X = np.arange(2, size, 1)
#N = np.random.normal(u, o, size=(size))
N = np.random.standard_cauchy(size)
print(N)
print(len(N))
estimator_expected_value = []
estimator_variance_1 = []
estimator_variance_2 = []
L = 50


for i in range(2,len(N)):
    estimator_expected_value.append(np.sum(N[:i]) / i)
    estimator_variance_1.append(np.sum(np.power(N[:i] - estimator_expected_value[i-2], 2)) / i)
    estimator_variance_2.append(np.sum(np.power(N[:i] - estimator_expected_value[i-2], 2)) / (i - 1))


plt.figure(1)
plt.plot(X, estimator_expected_value, '-', label="wartość estymatora")
plt.title("Estymator wartości oczekiwanej od N")
plt.ylabel("Wartość estymatora ")
plt.xlabel("Liczba wygenerowanych próbek")
plt.legend()

plt.figure(2)
plt.plot(X, estimator_variance_1, '-', label="wartość estymatora")
plt.title("Estymator wariancji obciążony od N")
plt.ylabel("Wartość estymatora ")
plt.xlabel("Liczba wygenerowanych próbek")
plt.legend()


plt.figure(3)
plt.plot(X, estimator_variance_2, '-', label="wartość estymatora")
plt.title("Estymator wariancji nieobciążony od N")
plt.ylabel("Wartość estymatora ")
plt.xlabel("Liczba wygenerowanych próbek")
plt.legend()

plt.show()