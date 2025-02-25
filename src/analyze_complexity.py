import time
import os
import matplotlib.pyplot as plt
import numpy as np
import csv
from fibonacci_turing import run_fibonacci

RESULTS_DIR = "results"
CSV_FILE = os.path.join(RESULTS_DIR, "execution_times.csv")
PLOT_FILE = os.path.join(RESULTS_DIR, "execution_plot.png")

def ensure_results_dir():
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)

def measure_execution_times(n_values, repetitions=5):
    ensure_results_dir()
    times = []

    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["n", "execution_time"])

        for n in n_values:
            exec_times = []
            for _ in range(repetitions):  # Repetimos varias veces para mayor precisión
                start_time = time.perf_counter()
                run_fibonacci()
                end_time = time.perf_counter()
                exec_times.append(end_time - start_time)

            avg_time = sum(exec_times) / repetitions  # Promedio de tiempos
            times.append(avg_time)
            writer.writerow([n, avg_time])

    print(f"Resultados guardados en {CSV_FILE}")
    return times

def plot_execution_times(n_values, times):
    plt.figure(figsize=(8, 5))
    plt.plot(n_values, times, marker='o', linestyle='-')
    plt.xlabel("Tamaño de n (Fibonacci)")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title("Tiempo de ejecución de la Máquina de Turing")
    plt.grid()

    plt.savefig(PLOT_FILE)
    print(f"Gráfica guardada en {PLOT_FILE}")
    plt.show()

if __name__ == "__main__":
    n_values = [2, 3, 4, 5, 6, 7, 8]
    times = measure_execution_times(n_values, repetitions=10)  # Más repeticiones para precisión
    plot_execution_times(n_values, times)
