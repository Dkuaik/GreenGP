import matplotlib.pyplot as plt
import numpy as np

class EvolutionPlotter:
    def __init__(self, x_values, y_values):
        self.x_values = x_values
        self.y_values = y_values
        self.fig, self.ax = plt.subplots(figsize=(12, 6))
        plt.ion()  # Modo interactivo
        
    def plot_evolution(self, individual, generation):
        """Grafica los datos reales vs las predicciones del mejor individuo."""
        self.ax.clear()
        
        # Datos reales
        self.ax.scatter(self.x_values, self.y_values, color='blue', alpha=0.5, label='Datos reales')
        
        # Predicciones del mejor individuo
        try:
            predictions = [individual.evaluate_x(x) for x in self.x_values]
            self.ax.plot(self.x_values, predictions, 'r-', label=f'Generación {generation}')
        except:
            print(f"Error al graficar generación {generation}")
        
        self.ax.set_title(f'Evolución del ajuste - Generación {generation}')
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.legend()
        self.ax.grid(True)
        
        # Mostrar el fitness y la función
        if hasattr(individual, 'fitness'):
            info_text = [
                f'Fitness: {individual.fitness:.6f}',
                f'Función: {individual.root.to_string()}'
            ]
            self.ax.text(0.02, 0.98, '\n'.join(info_text),
                        transform=self.ax.transAxes,
                        verticalalignment='top',
                        bbox=dict(facecolor='white', alpha=0.8))
        
        plt.pause(0.1)  # Pausa para actualización
        
    def save_plot(self, filename):
        """Guarda la última gráfica en un archivo."""
        self.fig.savefig(filename)
