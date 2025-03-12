import random
import numpy as np
from individuos.nodes import Node, operators, unary_operators  # Asegúrate de que tree.py contenga la clase Node y los operadores


class Individual:
    def __init__(self, depth=3):
        self.root = self.generate_tree(depth)
        self.fitness = None

    def generate_tree(self, depth):
        """Genera un árbol aleatorio de operaciones matemáticas."""
        if depth == 0:
            # Hoja: puede ser un número constante o la variable 'x'
            return Node(value=random.choice(['x', random.uniform(-10, 10)]))

        # Nodo interno: operador binario o unario
        operation = random.choice(list(operators.keys()))  
        
        if operation in unary_operators:
            return Node(operation, left=self.generate_tree(depth - 1))  # Solo un hijo para funciones unarias
        else:
            return Node(operation, left=self.generate_tree(depth - 1), right=self.generate_tree(depth - 1))  # Binario

    def get_random_node(self):
        """Selecciona un nodo aleatorio del árbol binario."""
        nodes = []

        def traverse(node):
            if node:
                nodes.append(node)
                traverse(node.left)
                traverse(node.right)

        traverse(self.root)

        return random.choice(nodes) if nodes else None

    def evaluate(self, x_value):
        """Evalúa la función con un valor de x."""
        if self.fitness is None:
            self.fitness = self.root.evaluate(x_value)
        return self.fitness
    
    def evaluate_x(self,x_values):
        return self.root.evaluate(x_values)

    def replace_with(self, node):
        """Reemplaza un nodo con otro del mismo tipo: 
        - Operadores binarios por otros binarios
        - Operadores unarios por otros unarios
        - Números por otros números aleatorios
        """

        if node is None:
            return
        
        if node.value in operators:  # Si es un operador
            if node.value in unary_operators:
                # Reemplazar por otro operador unario
                node.value = random.choice(list(unary_operators))
            else:
                # Reemplazar por otro operador binario
                bin_ops = operators.keys() - unary_operators
                node.value = random.choice(bin_ops)
        
        elif isinstance(node.value, (int, float)):  # Si es un número
            node.value = random.uniform(-10, 10)  # Nuevo número aleatorio

        elif node.value == 'x':  # Si es la variable 'x', no se reemplaza
            pass

