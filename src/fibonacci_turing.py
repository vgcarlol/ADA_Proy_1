from turing_machine import TuringMachine

def run_fibonacci():
    tm = TuringMachine("configs/fibonacci_config.json")
    result = tm.run()
    print("Resultado en la cinta:", result)
    tm.run(verbose=True)

if __name__ == "__main__":
    run_fibonacci()
