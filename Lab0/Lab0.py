import numpy as np
import matplotlib.pyplot as plt

generatedNumbers = []
z = 7
def RandomNumberGenerator(Seed,Amount):
    xn = Seed
    for i in range(Amount):
        generatedNumbers.append(xn)
        xn = z*xn - np.floor(z*xn)
        

seed = 0.99

RandomNumberGenerator(seed,1000)
print(generatedNumbers)
X = []
for i in range(1000):
    X.append(i)

print(len(X),len(generatedNumbers))
fig, (PLOT) = plt.subplots(1, 2)
title = "Seed = " + str(seed) + "  Z = " + str(z)
fig.suptitle(title)
PLOT[0].plot(X, generatedNumbers,'o')
PLOT[0].set_xlabel('Numer próbki')
PLOT[0].set_ylabel('Wartość próbki')
PLOT[1].hist(generatedNumbers, bins=50)
PLOT[1].set_xlabel('Wartość próbki')
PLOT[1].set_ylabel('Ilość próbek o danej wartości')
plt.show()
