# GreenGP - Programación Genética para Aproximación de Funciones

## Descripción
Sistema de programación genética que evoluciona expresiones matemáticas para aproximar funciones. Implementa un algoritmo evolutivo con operadores genéticos adaptables y visualización en tiempo real.

## Requisitos
```bash
requirements.txt
```

## Instalación
```bash
# Clonar el repositorio
git clone https://github.com/Dkuaik/GreenGP.git
cd GreenGP

# Crear y activar entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

## Estructura del Proyecto
```
GreenGP/
├── datos/
│   └── square_root_data.json    # Datos de entrenamiento
├── individuos/
│   ├── nodes.py                 # Implementación de nodos
│   └── individual.py            # Clase Individual
├── operadores/
│   └── EvolutionaryAlgorithmClassic.py
├── utils/
│   ├── plotting.py              # Visualización
│   └── comparación_mathteorical.py
├── experiments/
│   └── first_evolutionary_problem.py
└── main.py
```

## Uso

### Ejecución Básica
```bash
python main.py
```

### Parámetros Configurables
```python
population_size = 200    # Tamaño de la población
generations = 200       # Número de generaciones
mutation_rate = 0.4     # Tasa de mutación
crossover_rate = 0.8    # Tasa de cruce
elite_size = 5          # Cantidad de élites preservados
```

### Comparación con Función Teórica
```bash
python utils/comparación_mathteorical.py
```

## Características
- Evolución en tiempo real con visualización gráfica
- Elitismo para preservar mejores soluciones
- Operadores genéticos adaptativos
- Manejo seguro de operaciones matemáticas
- Múltiples operadores: +, -, *, /, ^, sin, cos, tan, log

## Resultados
Los resultados se guardan en:
```
resultados/graficas/
├── generacion_0.png
├── generacion_10.png
...
└── resultado_final.png
```

## Visualización
- Gráfica en tiempo real de la evolución
- Comparación entre datos reales y predicciones
- Visualización de la mejor función encontrada
- Estructura del árbol de expresiones

## Tips de Uso
1. Ajusta `population_size` según la complejidad del problema
2. Modifica `mutation_rate` si la convergencia es muy rápida/lenta
3. Usa `elite_size` para balancear exploración/explotación
4. Verifica los resultados en `resultados/graficas/`
