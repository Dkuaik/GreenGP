import random
import numpy as np
from individuos.nodes import Node, operators, unary_operators  # Asegúrate de que tree.py contenga la clase Node y los operadores


class Individual:
    def __init__(self, depth=3):
        self.root = self.generate_tree(depth)
        self.fitness = float('inf')  # Inicializar con el peor caso posible

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
    
    def evaluate_x(self, x_value):
        """Evalúa la función para un valor x específico."""
        return self.root.evaluate(x_value)
    
    def calculate_fitness(self, x_values, y_values):
        """Calcula el fitness del individuo usando MSE."""
        predictions = []
        for x in x_values:
            prediction = self.evaluate_x(x)
            if prediction is None:
                self.fitness = float('inf')
                return self.fitness
            predictions.append(prediction)
        
        predictions = np.array(predictions)
        self.fitness = np.mean((predictions - y_values) ** 2)
        return self.fitness

    def replace_with(self, old_node, new_node):
        """Reemplaza un nodo específico en el árbol con uno nuevo."""
        if old_node == self.root:
            self.root = new_node
        else:
            # Encuentra el nodo padre y reemplaza el hijo correspondiente
            nodes = []
            def find_parent(node):
                if node:
                    if node.left == old_node or node.right == old_node:
                        nodes.append(node)
                    find_parent(node.left)
                    find_parent(node.right)
            
            find_parent(self.root)
            if nodes:
                parent = nodes[0]
                if parent.left == old_node:
                    parent.left = new_node
                else:
                    parent.right = new_node

    def generate_compatible_node(self, target_node, depth):
        """Genera un nuevo nodo compatible con el nodo objetivo."""
        if isinstance(target_node.value, (int, float)):
            return Node(value=random.uniform(-10, 10))
        elif target_node.value == 'x':
            return Node(value='x')
        elif target_node.value in operators:
            if target_node.value in unary_operators:
                # Generar nuevo operador unario
                new_op = random.choice(list(unary_operators))
                return Node(new_op, left=self.generate_tree(depth - 1))
            else:
                # Generar nuevo operador binario
                binary_ops = set(operators.keys()) - unary_operators
                new_op = random.choice(list(binary_ops))
                return Node(new_op, 
                          left=self.generate_tree(depth - 1),
                          right=self.generate_tree(depth - 1))
        return None

    def __str__(self):
        """Devuelve una representación en cadena del individuo."""
        info = [
            "=== Individual Information ===",
            f"Fitness: {self.fitness if self.fitness is not None else 'Not evaluated'}",
            "Function:",
            self.root.to_string(),
            "\nTree structure:",
            self._get_tree_structure(),
            "=========================="
        ]
        return "\n".join(info)

    def _get_tree_structure(self, node=None, prefix="", is_last=True):
        """Helper method para visualizar la estructura del árbol."""
        if node is None:
            node = self.root
            
        tree_str = prefix + ("└── " if is_last else "├── ") + str(node.value) + "\n"
        
        if node.left:
            tree_str += self._get_tree_structure(
                node.left,
                prefix + ("    " if is_last else "│   "),
                node.right is None
            )
        if node.right:
            tree_str += self._get_tree_structure(
                node.right,
                prefix + ("    " if is_last else "│   "),
                True
            )
            
        return tree_str

