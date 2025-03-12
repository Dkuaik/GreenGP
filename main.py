import numpy as np
import json
from operadores.EvolutionaryAlgorithmClassic import EvolutionaryAlgorithmClassic

# Generar datos de entrenamiento (puedes reemplazar esto con datos reales)
def generate_data():
    x_values = np.linspace(-10, 10, 100)
    y_values = np.sin(x_values) + np.random.normal(0, 0.1, len(x_values))  # Función objetivo con ruido
    return x_values, y_values

if __name__ == "__main__":
    # Parámetros del algoritmo evolutivo
    population_size = 100
    generations = 50
    mutation_rate = 0.1
    crossover_rate = 0.7
    
    # Inicializar algoritmo
    ea = EvolutionaryAlgorithmClassic(population_size, generations, mutation_rate, crossover_rate)
    
    # Leer datos de entrada desde el archivo JSON
    with open('datos/square_root_data.json', 'r') as file:
        data = json.load(file)
        x_values = data['x_values']
        y_values = data['y_values']
    
    # Ejecutar evolución
    best_individual = ea.evolve(x_values, y_values)
    
    print("Mejor función encontrada:")
    print(best_individual)