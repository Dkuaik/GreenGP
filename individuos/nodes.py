import operator
import math
import numpy as np

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def evaluate(self, x_value):
        if isinstance(self.value, (int, float)):
            return self.value
        elif self.value == 'x':  # Soporte para la variable x
            return x_value
        elif self.value in operators:
            left_val = self.left.evaluate(x_value) if self.left else None
            right_val = self.right.evaluate(x_value) if self.right else None
            
            if left_val is None or (right_val is None and self.value not in unary_operators):
                return None  # Evita cálculos inválidos
            
            if self.value == '/' and right_val == 0:
                return None  # Evita divisiones por cero
            if self.value == 'log' and left_val <= 0:
                return None  # Evita logaritmos de valores no positivos
            if self.value == '^' and left_val < 0 and not right_val.is_integer():
                return None  # Evita raíces de números negativos que generan complejos
            
            if self.value in unary_operators:  # Si es una función unaria como sin, cos, log
                return operators[self.value](left_val)
            else:  # Si es una operación binaria
                return operators[self.value](left_val, right_val)
        else:
            raise ValueError(f"Unknown operator: {self.value}")
    
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

