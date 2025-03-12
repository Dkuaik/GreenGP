import random
import numpy as np
from individuos.invidual import Individual

class EvolutionaryAlgorithmClassic:

    def __init__(self, population_size=100, generations=50, mutation_rate=0.1, crossover_rate=0.7):
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.population = [Individual(depth=3) for _ in range(self.population_size)]
    
    def evaluate_population(self, x_values, y_values):
        """Evalúa la población calculando el error cuadrático medio (MSE) entre la predicción y los valores reales."""
        for individual in self.population:
            predictions = np.array([individual.evaluate_x(x) for x in x_values])
            individual.fitness = np.mean((predictions - y_values) ** 2)  # MSE como función de fitness

    def select_parents(self):
        """Selección por torneo: elige dos individuos y selecciona el mejor."""
        selected = []
        for _ in range(len(self.population)):
            i1, i2 = random.sample(self.population, 2)
            selected.append(i1 if i1.fitness < i2.fitness else i2)  # Menor MSE es mejor
        return selected
    
    def crossover(self, parent1, parent2):
        """Cruza dos individuos intercambiando subárboles."""
        if random.random() < self.crossover_rate:
            node1, node2 = parent1.root.get_random_node(), parent2.root.get_random_node()
            node1.swap(node2)  # Suponiendo que la clase Node tiene un método swap()
        return parent1, parent2
    
    def mutate(self, individual):
        """Muta un individuo reemplazando un subárbol por uno nuevo."""
        if random.random() < self.mutation_rate:
            mutation_node = individual.root.get_random_node()
            new_subtree = individual.generate_tree(depth=random.randint(1, 3))
            mutation_node.replace_with(new_subtree)  # Suponiendo que Node tiene replace_with()
    
    def evolve(self, x_values, y_values):
        """Ejecuta el algoritmo evolutivo."""
        for generation in range(self.generations):
            self.evaluate_population(x_values, y_values)
            parents = self.select_parents()
            next_generation = []
            
            for i in range(0, len(parents), 2):
                if i + 1 < len(parents):
                    offspring1, offspring2 = self.crossover(parents[i], parents[i+1])
                    self.mutate(offspring1)
                    self.mutate(offspring2)
                    next_generation.extend([offspring1, offspring2])
            
            self.population = next_generation
            best_individual = min(self.population, key=lambda ind: ind.fitness)
            print(f"Generation {generation}, Best Fitness: {best_individual.fitness}")

        return min(self.population, key=lambda ind: ind.fitness)


