import numpy as np
import json
import matplotlib.pyplot as plt
from operadores.EvolutionaryAlgorithmClassic import EvolutionaryAlgorithmClassic
from utils.plotting import EvolutionPlotter
import os

# Generar datos de entrenamiento (puedes reemplazar esto con datos reales)
def generate_data():
    x_values = np.linspace(-10, 10, 100)
    y_values = np.sin(x_values) + np.random.normal(0, 0.1, len(x_values))  # Función objetivo con ruido
    return x_values, y_values

if __name__ == "__main__":
    # Parámetros del algoritmo evolutivo
    population_size = 200
    generations = 200
    mutation_rate = 0.4
    crossover_rate = 0.8
    elite_size = 5
    
    # Crear directorio para gráficas si no existe
    os.makedirs('resultados/graficas', exist_ok=True)
    
    # Leer datos de entrada
    with open('datos/square_root_data.json', 'r') as file:
        data = json.load(file)
        x_values = np.array(data['x_values'])
        y_values = np.array(data['y_values'])
    
    # Inicializar plotter y algoritmo
    plotter = EvolutionPlotter(x_values, y_values)
    ea = EvolutionaryAlgorithmClassic(
        population_size=population_size,
        generations=generations,
        mutation_rate=mutation_rate,
        crossover_rate=crossover_rate,
        elite_size=elite_size
    )
    
    # Callback para graficar cada 10 generaciones
    def plot_callback(generation, best_individual):
        if generation % 10 == 0:
            plotter.plot_evolution(best_individual, generation)
            plotter.save_plot(f'resultados/graficas/generacion_{generation}.png')
    
    # Ejecutar evolución con callback
    best_individual = ea.evolve(x_values, y_values, callback=plot_callback)
    
    # Graficar resultado final
    plotter.plot_evolution(best_individual, generations)
    plotter.save_plot('resultados/graficas/resultado_final.png')
    plt.show()  # Mantener la última gráfica visible
    
    print("\nMejor función encontrada:")
    print(best_individual)