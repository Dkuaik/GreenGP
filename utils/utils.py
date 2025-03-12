import numpy as np

import matplotlib.pyplot as plt

def plot_individual(individual):
    x_values = np.linspace(-10, 10, 100)
    y_values = np.array([individual.evaluate(x) for x in x_values])
    plt.plot(x_values, y_values, label=f'f(x) = {individual.root.to_string()}')

def plot_population(population):
    plt.figure(figsize=(10, 6))
    for individual in population:
        plot_individual(individual)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Funciones generadas por individuos')
    plt.legend()
    plt.show()