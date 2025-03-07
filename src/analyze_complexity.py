import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

def compute_best_polynomial(x, y, max_power=5):
    best_r2 = -np.inf
    optimal_poly = None
    best_power = 0
    for degree in range(1, max_power + 1):
        coefficients = np.polyfit(x, y, degree)
        poly_func = np.poly1d(coefficients)
        predictions = poly_func(x)
        current_r2 = r2_score(y, predictions)
        if current_r2 > best_r2:
            best_r2 = current_r2
            optimal_poly = poly_func
            best_power = degree
    return optimal_poly, best_power

def perform_analysis(csv_filename="fibonacci_results.csv"):
    entradas = []
    tiempos = []
    salidas = []
    
    with open(csv_filename, "r") as file:
        lector = csv.reader(file)
        next(lector)  # Saltar encabezado
        for row in lector:
            # Orden: Cadena Entrada, Entrada Decimal, Tiempo (s), Salida Unaria, Salida Decimal
            entradas.append(float(row[1]))
            tiempos.append(float(row[2]))
            salidas.append(float(row[4]))
    
    entradas = np.array(entradas)
    tiempos = np.array(tiempos)
    salidas = np.array(salidas)
    
    # Ajustes polinómicos
    poly_time_vs_output, deg_time_output = compute_best_polynomial(salidas, tiempos)
    poly_time_vs_input, deg_time_input = compute_best_polynomial(entradas, tiempos)
    poly_output_vs_input, deg_output_input = compute_best_polynomial(entradas, salidas)
    
    x_fit_output = np.linspace(min(salidas), max(salidas), 100)
    y_fit_time_output = poly_time_vs_output(x_fit_output)
    
    x_fit_input = np.linspace(min(entradas), max(entradas), 100)
    y_fit_time_input = poly_time_vs_input(x_fit_input)
    y_fit_output_input = poly_output_vs_input(x_fit_input)
    
    # Crear una figura con 2 filas y 2 columnas de subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    
    # Subplot 1: Salida Decimal vs Tiempo
    axs[0,0].scatter(salidas, tiempos, color='blue', label="Datos")
    axs[0,0].plot(x_fit_output, y_fit_time_output, color='red', label=f"Ajuste (grado {deg_time_output})")
    axs[0,0].set_title("Salida Decimal vs Tiempo")
    axs[0,0].set_xlabel("Salida Decimal")
    axs[0,0].set_ylabel("Tiempo (s)")
    axs[0,0].grid(True)
    axs[0,0].legend()
    
    # Subplot 2: Entrada Decimal vs Tiempo
    axs[0,1].scatter(entradas, tiempos, color='blue', label="Datos")
    axs[0,1].plot(x_fit_input, y_fit_time_input, color='red', label=f"Ajuste (grado {deg_time_input})")
    axs[0,1].set_title("Entrada Decimal vs Tiempo")
    axs[0,1].set_xlabel("Entrada Decimal")
    axs[0,1].set_ylabel("Tiempo (s)")
    axs[0,1].grid(True)
    axs[0,1].legend()
    
    # Subplot 3: Entrada Decimal vs Salida Decimal
    axs[1,0].scatter(entradas, salidas, color='green', label="Datos")
    axs[1,0].plot(x_fit_input, y_fit_output_input, color='red', label=f"Ajuste (grado {deg_output_input})")
    axs[1,0].set_title("Entrada Decimal vs Salida Decimal")
    axs[1,0].set_xlabel("Entrada Decimal")
    axs[1,0].set_ylabel("Salida Decimal")
    axs[1,0].grid(True)
    axs[1,0].legend()
    
    # Subplot 4: Entrada vs Salida en Escala Logarítmica
    axs[1,1].scatter(entradas, salidas, color='purple', label="Datos")
    axs[1,1].plot(x_fit_input, y_fit_output_input, color='red', label=f"Ajuste (grado {deg_output_input})")
    axs[1,1].set_yscale("log")
    axs[1,1].set_title("Entrada vs Salida (Escala Log)")
    axs[1,1].set_xlabel("Entrada Decimal")
    axs[1,1].set_ylabel("Salida Decimal (log)")
    axs[1,1].grid(True)
    axs[1,1].legend()
    
    plt.tight_layout()
    plt.show()
    
    print(f"Ajuste Salida-Tiempo: Grado {deg_time_output}, Función: {poly_time_vs_output}")
    print(f"Ajuste Entrada-Tiempo: Grado {deg_time_input}, Función: {poly_time_vs_input}")
    print(f"Ajuste Entrada-Salida: Grado {deg_output_input}, Función: {poly_output_vs_input}")

if __name__ == "__main__":
    perform_analysis()
