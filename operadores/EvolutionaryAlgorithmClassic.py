import random
import numpy as np
from individuos.invidual import Individual
import copy

class EvolutionaryAlgorithmClassic:

    def __init__(self, population_size=100, generations=50, mutation_rate=0.1, crossover_rate=0.7, elite_size=2):
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elite_size = elite_size
        self.population = [Individual(depth=random.randint(2, 4)) for _ in range(self.population_size)]  # Profundidad variable
        self.best_ever = None
        self.best_fitness = float('inf')
    
    def evaluate_population(self, x_values, y_values):
        """Evalúa la población calculando el fitness de cada individuo."""
        for individual in self.population:
            individual.calculate_fitness(x_values, y_values)

    def select_parents(self):
        """Selección por torneo mejorada con tamaño de torneo variable."""
        selected = []
        tournament_size = 3  # Aumentar presión selectiva
        
        for _ in range(len(self.population)):
            tournament = random.sample(self.population, tournament_size)
            winner = min(tournament, key=lambda ind: ind.fitness)
            selected.append(winner)
        
        return selected
    
    def crossover(self, parent1, parent2):
        """Cruza dos individuos intercambiando subárboles."""
        if random.random() < self.crossover_rate:
            node1, node2 = parent1.get_random_node(), parent2.get_random_node()
            node1.swap(node2)  # Suponiendo que la clase Node tiene un método swap()
        return parent1, parent2
    
    def mutate(self, individual):
        """Muta un individuo reemplazando un subárbol por uno nuevo compatible."""
        if random.random() < self.mutation_rate:
            mutation_node = individual.get_random_node()
            new_subtree = individual.generate_compatible_node(mutation_node, depth=random.randint(1, 3))
            mutation_node.replace_with(new_subtree)
    
    def evolve(self, x_values, y_values, callback=None):
        """Ejecuta el algoritmo evolutivo con elitismo."""
        generations_without_improvement = 0
        
        for generation in range(self.generations):
            self.evaluate_population(x_values, y_values)
            
            # Encontrar el mejor de la generación actual
            current_best = min(self.population, key=lambda ind: ind.fitness)
            
            # Actualizar el mejor global si es necesario
            if current_best.fitness < self.best_fitness:
                self.best_ever = copy.deepcopy(current_best)  # Hacer copia profunda
                self.best_fitness = current_best.fitness
                generations_without_improvement = 0
            else:
                generations_without_improvement += 1
            
            # Ordenar población y obtener élite
            sorted_population = sorted(self.population, key=lambda ind: ind.fitness)
            elite = [copy.deepcopy(ind) for ind in sorted_population[:self.elite_size]]
            
            # Selección y reproducción
            parents = self.select_parents()
            next_generation = []
            
            # Asegurar que el mejor global siempre está presente
            next_generation.append(copy.deepcopy(self.best_ever))
            
            # Agregar élite
            next_generation.extend(elite)
            
            # Crear el resto de la nueva población
            while len(next_generation) < self.population_size:
                if len(parents) >= 2:
                    p1, p2 = random.sample(parents, 2)
                    offspring1, offspring2 = copy.deepcopy(p1), copy.deepcopy(p2)
                    self.crossover(offspring1, offspring2)
                    
                    # Mutar offspring con probabilidad variable
                    if random.random() < self.mutation_rate * (1 + generations_without_improvement * 0.1):
                        self.mutate(offspring1)
                    if random.random() < self.mutation_rate * (1 + generations_without_improvement * 0.1):
                        self.mutate(offspring2)
                    
                    next_generation.extend([offspring1, offspring2])
            
            # Ajustar tamaño de población si es necesario
            self.population = next_generation[:self.population_size]
            
            print(f"Generation {generation}")
            print(f"Current Best Fitness: {current_best.fitness}")
            print(f"Best Ever Fitness: {self.best_fitness}")
            print("Best Solution:")
            print(self.best_ever)
            print("-" * 50)
            
            if callback:
                callback(generation, self.best_ever)
            
            # Criterio de convergencia
            if generations_without_improvement > 20:
                print("Convergencia detectada - terminando evolución")
                break
        
        return self.best_ever


