from turing_machine import TuringMachine
import json

def run_fibonacci(n, verbose=True):
    # Cargar la configuración existente
    with open("configs/fibonacci_config.json", "r") as f:
        config = json.load(f)

    # Modificar la cinta inicial para reflejar el valor de n
    config["initial_tape"] = "1" * n + "_1"

    # Guardar la configuración actualizada temporalmente
    temp_config_path = "configs/temp_fibonacci_config.json"
    with open(temp_config_path, "w") as f:
        json.dump(config, f)

    # Ejecutar la máquina de Turing con la configuración modificada
    tm = TuringMachine(temp_config_path)
    result = tm.run(verbose=verbose)  # Silenciar salida si se está midiendo tiempos

    if verbose:
        print(f"Resultado en la cinta para n={n}: {result}")
    return result

if __name__ == "__main__":
    run_fibonacci(5)  # Ejemplo con n=5
