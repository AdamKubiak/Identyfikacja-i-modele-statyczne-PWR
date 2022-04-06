from distutils.log import error
import numpy as np
import matplotlib.pyplot as plt
from numpy import array
from numpy import vectorize

IMG_SIZE = (15, 7)


def sampel_mean(samples):
    return np.sum(samples)/len(samples)

def unadjusted_variance_estimator(samples, mean_value):
    return np.sum((samples - mean_value)**2)/ len(samples)

def adjusted_variance_estimator(samples, mean_value):
    return np.sum((samples - mean_value)**2)/ (len(samples)-1)

def plot_distribution_histograms(values):
    plt.figure("p3", figsize=IMG_SIZE)
    plt.hist(values[0], density=True,label = 'Rozklad normalny',bins = 30,alpha=0.5)    
    plt.hist(values[1], density=True, label= "Rozkładu Cauchy", bins =30,alpha = 0.5)
    plt.ylabel('Ilość próbek o danej wartości')
    plt.xlabel('Wartość próbki')
    plt.title(f'Porównanie histogramu rozkładu normalnego oraz rozkładu Cauchy\'ego dla {len(values[0])} próbek')
    plt.legend()
    plt.grid(color = 'black', linestyle = '--', linewidth = 0.5)
    #plt.savefig(f'img/lab3/Hist_normal_cauchy_probek_{len(values[0])}')
    plt.show()

def plot_error(x, y, l, rand_method, equation_name):
    plt.figure("p3", figsize=IMG_SIZE)
    plt.plot(x,y)
    plt.xlabel('Ilość próbek[n]')
    plt.ylabel('Wartość błędu')
    plt.title(f'Wykres błędu empirycznego danego wzorem powyżej dla parametru L = {l} dla rozkładu {rand_method}')
    plt.grid(color = 'black', linestyle = '--', linewidth = 0.5)
    #plt.savefig(f'img/lab3/Wykres_bledu_l_{l}_metoda_{equation_name}_losowa_{rand_method}')
    plt.show()

def get_cauchy_limted_values(n):
    x = np.random.standard_cauchy(n)
    x = x[(x >-10) & (x < 10)]
    return x


def count_variance_error(values, expected_value=0):
    return (sampel_mean(values) - expected_value)**2


def count_unadjusted_variance_estimator_error(values, variance=1):
    return (unadjusted_variance_estimator(values,sampel_mean(values))**2 - variance)**2

def count_adjusted_variance_estimator_error(values, variance=1):
    return (adjusted_variance_estimator(values,sampel_mean(values))**2  - variance)**2


def variance_error(l_array, err_estimator=count_variance_error):
    result = 0
    for i in l_array:
        result += err_estimator(i)

    return(result/len(l_array))

def get_error_for_n(n, l = 15, err_estimator=count_variance_error):
    l = np.random.normal(0, 1, (l,n))
    return variance_error(l, err_estimator)


if __name__ == '__main__':
    n = [100, 1000, 10000]
    for i in n:
        print(i)
        normal = np.random.normal(0, 1, i)
        normal_mean = sampel_mean(normal)
        print('Normal')
        print(f'Średnia {normal_mean}')
        print(f'Estymator 1 {unadjusted_variance_estimator(normal,normal_mean)}')
        print(f'Estymator 2 {adjusted_variance_estimator(normal,normal_mean)}')
        cauchy = np.random.standard_cauchy(i)
        cauchy_mean = sampel_mean(cauchy)
        print('Cauchy')
        print(f'Średnia {cauchy_mean}')
        print(f'Estymator 1 {unadjusted_variance_estimator(cauchy, cauchy_mean)}')
        print(f'Estymator 2 {adjusted_variance_estimator(cauchy, cauchy_mean)}')


    mi, sigma = 0, 1

    values = np.array([(np.random.normal(mi, sigma, i), get_cauchy_limted_values(i)) for i in n], dtype=object)
    for i in range(0,len(n)):
        plot_distribution_histograms(values[i])

    normal_name = "normalnego N(0,1)"

    x = np.linspace(2,201,200, dtype='int')
    f = np.vectorize(get_error_for_n)

    error_value_mean_l15_2 = f(x,20,count_unadjusted_variance_estimator_error)
    plot_error(x, error_value_mean_l15_2, 20, normal_name, "wzór_drugi")
    error_value_mean_l80_2 = f(x,60,count_unadjusted_variance_estimator_error)
    plot_error(x, error_value_mean_l80_2, 60, normal_name, "wzór_drugi")

    error_value_mean_l15 = f(x)
    plot_error(x, error_value_mean_l15, 20, normal_name, "wzór_pierwszy")
    error_value_mean_l80 = f(x,60)
    plot_error(x, error_value_mean_l80, 60, normal_name, "wzór_pierwszy")

    error_value_mean_l15_3 = f(x,20,count_adjusted_variance_estimator_error)
    plot_error(x, error_value_mean_l15_3, 20, normal_name, "wzór_trzeci")
    error_value_mean_l80_3 = f(x,60,count_adjusted_variance_estimator_error)
    plot_error(x, error_value_mean_l80_3, 60, normal_name, "wzór_trzeci")
