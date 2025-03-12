import operator
import math
import numpy as np

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def evaluate(self, x_value, max_depth=10, current_depth=0):
        if current_depth > max_depth:
            return None  # Evita desbordamiento por recursión excesiva
        
        try:
            if isinstance(self.value, (int, float)):
                return self.value
            elif self.value == 'x':  # Soporte para la variable x
                return x_value
            elif self.value in operators:
                left_val = self.left.evaluate(x_value, max_depth, current_depth + 1) if self.left else None
                right_val = self.right.evaluate(x_value, max_depth, current_depth + 1) if self.right else None
                
                # Validaciones previas
                if left_val is None or (right_val is None and self.value not in unary_operators):
                    return None

                # Validaciones específicas por operador
                try:
                    if self.value == '/':
                        if abs(right_val) < 1e-10:  # Evitar división por números muy cercanos a cero
                            return None
                    elif self.value == 'log':
                        if left_val <= 0:
                            return None
                    elif self.value == '^':
                        if left_val == 0 and right_val <= 0:  # 0^0 o 0^negativo
                            return None
                        if left_val < 0 and not float(right_val).is_integer():  # base negativa con exponente no entero
                            return None
                        if abs(right_val) > 100:  # Limitar exponentes muy grandes
                            return None
                    elif self.value in ['sin', 'cos', 'tan']:
                        if abs(left_val) > 1e6:  # Limitar entrada a funciones trigonométricas
                            return None
                        if self.value == 'tan' and abs(math.cos(left_val)) < 1e-10:  # Evitar tangente cerca de π/2
                            return None

                    # Ejecutar la operación
                    if self.value in unary_operators:
                        result = operators[self.value](left_val)
                    else:
                        result = operators[self.value](left_val, right_val)

                    # Validar resultado
                    if result is None or not np.isfinite(result):
                        return None
                    if abs(result) > 1e10:  # Limitar resultados muy grandes
                        return None
                    
                    return result

                except (ValueError, ZeroDivisionError, OverflowError):
                    return None
            else:
                raise ValueError(f"Unknown operator: {self.value}")
                
        except (ValueError, OverflowError, ZeroDivisionError):
            return None
    
    def to_string(self):
        if isinstance(self.value, (int, float)):
            return str(self.value)
        elif self.value == 'x':
            return 'x'
        elif self.value in unary_operators:
            return f"{self.value}({self.left.to_string()})"
        else:
            return f"({self.left.to_string()} {self.value} {self.right.to_string()})"
    
    def swap(self, other):
        self.value, other.value = other.value, self.value
        self.left, other.left = other.left, self.left
        self.right, other.right = other.right, self.right
        return self, other

    def is_compatible(self, other):
        """Verifica si dos nodos son compatibles para reemplazo."""
        # Ambos son valores numéricos
        if isinstance(self.value, (int, float)) and isinstance(other.value, (int, float)):
            return True
        # Ambos son la variable x
        if self.value == 'x' and other.value == 'x':
            return True
        # Ambos son operadores del mismo tipo (unario o binario)
        if self.value in operators and other.value in operators:
            return (self.value in unary_operators) == (other.value in unary_operators)
        return False

    def replace_with(self, other):
        """Reemplaza este nodo por otro solo si son compatibles."""
        if not self.is_compatible(other):
            raise ValueError("Cannot replace nodes of different types")
        
        self.value = other.value
        if other.left:
            self.left = Node(other.left.value, other.left.left, other.left.right)
        if other.right and self.value not in unary_operators:
            self.right = Node(other.right.value, other.right.left, other.right.right)
        return self

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'log': math.log
}


unary_operators = {'sin', 'cos', 'tan', 'log'}

