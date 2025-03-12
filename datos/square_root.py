import json
import numpy as np

# Generar 150 puntos entre -10 y 10
x_values = np.linspace(0, 10, 150)
# Calcular la raíz cuadrada de los valores absolutos
y_values = np.sqrt(np.abs(x_values))

# Crear un diccionario con los datos
data = {"x_values": x_values.tolist(), "y_values": y_values.tolist()}

# Guardar los datos en un archivo JSON
with open('datos/square_root_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)