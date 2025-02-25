import json

class TuringMachine:
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            config = json.load(f)

        self.original_tape = list(config["initial_tape"])  # Guardar cinta original
        self.tape = self.original_tape[:]
        self.head = config["initial_head_position"]
        self.state = config["start_state"]
        self.accept_state = config["accept_state"]
        self.transitions = {tuple(k.split(',')): v for k, v in config["transitions"].items()}

    def reset(self):
        self.tape = self.original_tape[:]
        self.head = 0
        self.state = "q0"

    def step(self):
        symbol = self.tape[self.head]

        if (self.state, symbol) in self.transitions:
            new_symbol, move, new_state = self.transitions[(self.state, symbol)]
            self.tape[self.head] = new_symbol

            # Imprimir información del paso
            print(f"Paso: Estado={self.state}, Símbolo={symbol}, Nueva cinta={''.join(self.tape)}, Cabeza={self.head}, Nuevo estado={new_state}")

            # Mover la cabeza de lectura
            if move == 'R':
                self.head += 1
                if self.head >= len(self.tape):  # Expande la cinta si es necesario
                    self.tape.append('_')
            elif move == 'L':
                self.head -= 1
                if self.head < 0:
                    self.tape.insert(0, '_')
                    self.head = 0

            self.state = new_state
        else:
            return False  # No hay transición, se detiene
        return True

    def run(self, verbose=True):
        step_count = 0  # Contador de pasos

        while self.state != self.accept_state:
            if verbose:
                print(f"Paso {step_count}: Estado={self.state}, Cabeza={self.head}, Cinta={''.join(self.tape)}")
            if not self.step():
                break
            step_count += 1

            # Evitar bucles infinitos
            if step_count > 100:
                print("Se ha alcanzado el límite de pasos sin llegar al estado de aceptación.")
                break

        return ''.join(self.tape).strip('_')

if __name__ == "__main__":
    tm = TuringMachine("../configs/fibonacci_config.json")
    result = tm.run(verbose=True)
    print("\nResultado final en la cinta:", result)
