def get_starting_number():
    while True:
        try:
            initial_number = int(input("Ievadi sākuma skaitli: ").strip())
            if initial_number > 0:
                return initial_number
            else:
                print("Skaitlim jābūt pozitīvam.")
        except ValueError:
            print("Lūdzu, ievadi derīgu skaitli.")

def get_starting_player():
    while True:
        starter = input("Kas sāk spēli? (1 - Cilvēks, 2 - Dators): ").strip()
        if starter == "1":
            return True
        elif starter == "2":
            return False
        else:
            print("Nederīga ievade. Lūdzu, ievadi 1 vai 2.")

def get_algorithm_choice():
    print("Izvēlies algoritmu:")
    print("1 - Alpha-Beta")
    print("2 - Minimax")
    
    while True:
        algorithm_choice = input("Ievadi 1 vai 2: ").strip()
        
        if algorithm_choice == "1":
            use_alpha_beta = True
            use_minimax = False
            return use_alpha_beta, use_minimax
        elif algorithm_choice == "2":
            use_alpha_beta = False
            use_minimax = True
            return use_alpha_beta, use_minimax
        else:
            print("Nederīga ievade. Lūdzu, ievadi 1 vai 2.")

def display_initial_state(state):
    print(f"\nSākuma stāvoklis: Skaitlis={state.number}, Cilvēka punkti={state.human_score}, Datora punkti={state.ai_score}")

def get_human_move():
    print("\nTavs gājiens!")
    while True:
        multiplier = input("Izvēlies reizinātāju (2 vai 3): ").strip()
        if multiplier in ["2", "3"]:
            return int(multiplier)
        else:
            print("Nederīga ievade. Lūdzu, ievadi 2 vai 3.")

def display_human_move(state, multiplier):
    print(f"Tavs gājiens: {state.number} (reizinātājs: {multiplier}, Cilvēka punkti={state.human_score}, Datora punkti={state.ai_score})")

def prompt_for_ai_move():
    input("\nVai vēlies redzēt datora gājienu? (spied Enter, lai turpinātu) ")
    print("\nDatora gājiens...")

def display_ai_move(state, multiplier):
    print(f"Datora gājiens: {state.number} (reizinātājs: {multiplier}, Cilvēka punkti={state.human_score}, Datora punkti={state.ai_score})")

def display_game_end(state):
    print("\nSpēle beigusies!")
    print(f"Gala rezultāts: Cilvēka punkti={state.human_score}, Datora punkti={state.ai_score}")
    
    if state.human_score < state.ai_score:
        print("Tu uzvarēji!")
    elif state.human_score > state.ai_score:
        print("Dators uzvarēja!")
    else:
        print("Neizšķirts!")

def display_game_tree(state, max_depth, current_depth=0, prefix=""):
    if current_depth == 0:
        print("Spēles koks:")
        
    print(f"{prefix}Move {current_depth}: Skaitlis({state.number}), Cilvēks({state.human_score}), Ai({state.ai_score})")
    
    if current_depth >= max_depth or state.number >= 1000:
        return
    
    next_states = state.generate_next_states()

    for i in range(len(next_states)):
        if i == len(next_states) - 1:
            branch_prefix = "└── "  # Last branch
        else:
            branch_prefix = "├── "  # Intermediate branch
        
        display_game_tree(next_states[i], max_depth, current_depth + 1, prefix + branch_prefix)