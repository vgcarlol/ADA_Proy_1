from fibonacci_turing import run_fibonacci
from analyze_complexity import measure_execution_times, plot_execution_times

if __name__ == "__main__":
    print("Ejecutando Máquina de Turing para Fibonacci...")
    run_fibonacci()

    print("\nAnalizando tiempos de ejecución...")
    n_values = [2, 3, 4, 5, 6]
    times = measure_execution_times(n_values)
    plot_execution_times(n_values, times)
