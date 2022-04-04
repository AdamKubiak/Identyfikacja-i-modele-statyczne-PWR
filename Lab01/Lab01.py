import numpy as np
import matplotlib.pyplot as plt



#Podpunkt 1
#gęstość prawdopodobieństwa
f1 = lambda x: (2*x) * (x<=1) * (x>=0)

#dystrybuanta 
f2 = lambda x: (x**2) * (x <= 1) * (x >= 0) + (x > 1)

#odwrotna dystrybuanta
f3 = lambda x: (np.sqrt(x)) * (x <= 1) * (x >= 0)
##################################################################################
#Podpunkt 2
#gęstość prawdopodobieństwa
f4 = lambda x: (x + 1)  * (x < 0)   *  (x > -1)                 +   (-x+1)  * (x >= 0) * (x < 1)

#dystrybuanta 
f5 = lambda x: (0.5 + x + x**2/2)   *  (x < 0) * (x > -1)       +   (0.5 + x - x**2/2) * (x >= 0) * (x < 1) + (x >= 1)

#odwrotna dystrybuanta
f6 = lambda x: (np.sqrt(x * 2) - 1) *  (x >= 0) * (x <= 0.5)    +   (1 - np.sqrt(2 - x * 2)) * (x > 0.5) * (x <= 1) - (x < -1)
#################################################################################
#Podpunkt 3
#gęstość prawdopodobieństwa
f7 = lambda x:  (np.power(np.e, -x)) * (x >= 0)

#dystrybuanta 
f8 = lambda x: 1-(np.power(np.e, -x)) * (x >= 0)

#odwrotna dystrybuanta
f9 = lambda x: -(np.log(1 - x)) * (x >= 0)
#################################################################################
#Podpunkt 4
#gęstość prawdopodobieństwa
f10 = lambda x: 0.5 * np.power(np.e, -np.abs(x))
#dystrybuanta 
f11 = lambda x: 0.5 + 0.5 * (1 - np.power(np.e, -np.abs(x))) * (x >= 0) - 0.5 * (1 - np.power(np.e, -np.abs(x))) * (x < 0)
#odwrotna dystrybuanta
f12 = lambda x: -np.log(1 - x) * (x >= 0) + np.log(1 + x) * (x < 0)

x = np.arange(0, 1, 0.00001)
y = [f1(x),f2(x),f3(x)]
fig, (PLOTS) = plt.subplots(2, 2)
fig, (PLOTS0) = plt.subplots(2, 2)
PLOTS[0][0].hist(f3(x), density=True, label="Podpunkt 1")
PLOTS[0][0].plot(x,y[0],label='Gęstość prawdopodobieństwa')
PLOTS[0][0].plot(x,y[1],label='Dystrybuanta')
PLOTS[0][0].plot(x,y[2],label='Odwrotna dystrybuanta')
PLOTS[0][0].set_xlabel('Liczba pseudolosowa')
PLOTS[0][0].set_ylabel('Ilość próbek')
PLOTS[0][0].legend()

x = np.arange(-1, 1, 0.00001)
y.clear()
y = [f4(x),f5(x),f6(x)]

PLOTS[0][1].hist(f6(x), density=True, label="Podpunkt 2")
PLOTS[0][1].plot(x,y[0],label='Gęstość prawdopodobieństwa')
PLOTS[0][1].plot(x,y[1],label='Dystrybuanta')
PLOTS[0][1].plot(x,y[2],label='Odwrotna dystrybuanta')
PLOTS[0][1].set_xlabel('Liczba pseudolosowa')
PLOTS[0][1].set_ylabel('Ilość próbek')
PLOTS[0][1].legend()

x = np.arange(0, 6, 0.00001)
y.clear()
y = [f7(x),f8(x),f9(x)]
PLOTS[1][0].hist(f9(x), density=True, label="Podpunkt 3", range=(0,8))
PLOTS[1][0].plot(x,y[0],label='Gęstość prawdopodobieństwa')
PLOTS[1][0].plot(x,y[1],label='Dystrybuanta')
PLOTS[1][0].plot(x,y[2],label='Odwrotna dystrybuanta')
PLOTS[1][0].set_xlabel('Liczba pseudolosowa')
PLOTS[1][0].set_ylabel('Ilość próbek')
PLOTS[1][0].legend()

x = np.arange(-5, 5, 0.00001)
y.clear()
y = [f10(x),f11(x),f12(x)]
PLOTS0[1][1].hist(f12(x), density=True, label="Podpunkt 4", range=(-5,5))
PLOTS[1][1].plot(x,y[0],label='Gęstość prawdopodobieństwa')
PLOTS[1][1].plot(x,y[1],label='Dystrybuanta')
PLOTS[1][1].plot(x,y[2],label='Odwrotna dystrybuanta')
PLOTS[1][1].set_xlabel('Liczba pseudolosowa')
PLOTS[1][1].set_ylabel('Ilość próbek')
PLOTS[1][1].legend()

plt.show()
