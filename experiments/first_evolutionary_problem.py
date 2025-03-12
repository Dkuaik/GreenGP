from operadores.EvolutionaryAlgorithmClassic import *
import json

# Leer los datos desde el archivo JSON
with open('datos/square_root_data.json', 'r') as json_file:
    data = json.load(json_file)

print(data)



first_atempt = EvolutionaryAlgorithmClassic()
first_atempt.evolve(data['x_values'],data['y_values'])