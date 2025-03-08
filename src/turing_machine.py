import yaml

class ConfigReader:
    def __init__(self, config_path):
        self.config_path = config_path
        self.data = {}
        self.load_config()
        self.extract_parameters()
        
    def load_config(self):
        with open(self.config_path, 'r') as file:
            self.data = yaml.safe_load(file)
    
    def extract_parameters(self):
        # Usamos la estructura de tu YAML
        q_states = self.data.get("q_states", {})
        self.states = q_states.get("q_list", [])
        self.start_state = q_states.get("initial", "")
        self.end_state = q_states.get("final", "")
        self.input_symbols = self.data.get("alphabet", [])
        self.tape_symbols = self.data.get("tape_alphabet", [])
        self.sim_inputs = self.data.get("simulation_strings", [])
        transitions_list = self.data.get("delta", [])
        
        self.transitions = {}
        for trans in transitions_list:
            key = (trans["params"]["initial_state"], trans["params"]["tape_input"])
            value = (
                trans["output"]["final_state"],
                trans["output"]["tape_output"],
                trans["output"]["tape_displacement"]
            )
            self.transitions[key] = value

class TuringMachine:
    def __init__(self, states, start_state, end_state, input_symbols, tape_symbols, transitions):
        self.states = states
        self.start_state = start_state
        self.end_state = end_state
        self.input_symbols = input_symbols
        self.tape_symbols = tape_symbols
        self.transitions = transitions
        self.reset_machine()

    def reset_machine(self):
        self.tape = []
        self.head_index = 0
        self.current_state = self.start_state
        self.error = ""
    
    def load_tape(self, word):
        self.tape = list(word)
        self.current_state = self.start_state
        self.head_index = 0
        self.error = ""
    
    def single_step(self):
        if self.head_index < 0:
            self.tape.insert(0, "B")
            self.head_index = 0
        if self.head_index >= len(self.tape):
            self.tape.append("B")
        
        current_symbol = self.tape[self.head_index]
        if (self.current_state, current_symbol) not in self.transitions:
            self.error = "Transición no definida para el estado y símbolo actual."
            return False
        
        next_state, write_symbol, move_direction = self.transitions[(self.current_state, current_symbol)]
        self.tape[self.head_index] = write_symbol
        if move_direction == "R":
            self.head_index += 1
        elif move_direction == "L":
            self.head_index -= 1
            if self.head_index < 0:
                self.tape.insert(0, "B")
                self.head_index = 0
        self.current_state = next_state
        return True
    
    def run_machine(self):
        while True:
            if self.current_state == self.end_state:
                # Imprimir la cinta final (sin espacios en blanco "B")
                final_word = "".join(ch for ch in self.tape if ch != "B")
                print(f"Cinta transformada final: {final_word}")
                return True
            if not self.single_step():
                return False

    def display_tape(self):
        tape_str = ''.join(self.tape)
        if 0 <= self.head_index < len(self.tape):
            return tape_str[:self.head_index] + "[" + tape_str[self.head_index] + "]" + tape_str[self.head_index+1:]
        else:
            return "[B]"
