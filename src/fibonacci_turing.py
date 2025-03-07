import time
import csv
from turing_machine import ConfigReader, TuringMachine

def procesar_cadena(cadena, maquina):
    """Procesa una cadena de entrada y retorna un diccionario con los resultados."""
    # Convertir la entrada a valor decimal (si la cadena es "Z", se interpreta como 0)
    valor_entrada = 0 if cadena == "Z" else len(cadena)
    
    maquina.load_tape(cadena)
    inicio = time.perf_counter()
    maquina.run_machine()
    fin = time.perf_counter()
    
    tiempo_ejecucion = fin - inicio
    # Obtener la salida ignorando los espacios en blanco (marcados como "B")
    salida = "".join(c for c in maquina.tape if c != "B")
    valor_salida = 0 if salida == "Z" else len(salida)
    
    return {
        "cadena": cadena,
        "entrada": valor_entrada,
        "tiempo": tiempo_ejecucion,
        "salida": salida,
        "salida_decimal": valor_salida
    }

def simular_fibonacci(config_path="configs/fibonacci.yml", output_csv="fibonacci_results.csv"):
    # Cargar la configuración y crear la máquina
    config = ConfigReader(config_path)
    maquina = TuringMachine(
        config.states,
        config.start_state,
        config.end_state,
        config.input_symbols,
        config.tape_symbols,
        config.transitions
    )
    
    resultados = []
    for cad in config.sim_inputs:
        print(f"\nProcesando cadena: {cad}")
        datos = procesar_cadena(cad, maquina)
        print(f"Equivalente decimal: {datos['entrada']}")
        print(f"Salida unaria: {datos['salida']}")
        print(f"Salida decimal: {datos['salida_decimal']}")
        print(f"Tiempo transcurrido: {datos['tiempo']:.6f} s")
        resultados.append(datos)
    
    # Escribir resultados en un CSV
    with open(output_csv, 'w', newline='') as f:
        campos = ["cadena", "entrada", "tiempo", "salida", "salida_decimal"]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for res in resultados:
            escritor.writerow(res)

if __name__ == "__main__":
    simular_fibonacci()
