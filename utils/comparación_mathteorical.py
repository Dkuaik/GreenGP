import json
import numpy as np
import matplotlib.pyplot as plt

def approximate_sqrt(x):
    """
    Aproxima la raíz cuadrada de x usando una expresión algebraica.
    """
    return (1+((x-1)/2)-((x-1)**2/8))

def load_data(file_path):
    """
    Carga los datos desde un archivo JSON.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def compare_sqrt_approximations(data):
    """
    Compara las aproximaciones de la raíz cuadrada con los datos reales.
    """
    x_values = np.array(data['x_values'])
    y_values = np.array(data['y_values'])  # Cambiado de sqrt_values a y_values
    approx_sqrt_values = approximate_sqrt(x_values)

    plt.figure(figsize=(12, 6))
    plt.scatter(x_values, y_values, label='Datos reales', color='blue', alpha=0.5, s=20)
    plt.plot(x_values, approx_sqrt_values, label='Raíz cuadrada teórica', color='red', linestyle='--')
    plt.xlabel('Valores de X')
    plt.ylabel('Valores de Y')
    plt.title('Comparación entre datos reales y raíz cuadrada teórica')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Calcular el error cuadrático medio (MSE)
    mse = np.mean((y_values - approx_sqrt_values) ** 2)
    print(f"Error cuadrático medio (MSE): {mse}")

if __name__ == "__main__":
    data = load_data('/home/kuaik/Documents/projects/GreenGP/datos/square_root_data.json')
    compare_sqrt_approximations(data)