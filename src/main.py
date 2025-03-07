from fibonacci_turing import simular_fibonacci
from analyze_complexity import perform_analysis

def main():
    print("Ejecutando simulación de la máquina de Turing (Fibonacci)...")
    simular_fibonacci()
    print("\nIniciando análisis de complejidad...")
    perform_analysis()

if __name__ == "__main__":
    main()
