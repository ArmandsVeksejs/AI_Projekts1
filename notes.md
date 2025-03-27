Okay, so you have a different file structure in mind. Let's reorganize based on your requirements:

Existing files:
1. game_tree.py - Contains GameState class and print_game_tree
2. algoritmi.py - Contains AI algorithms like get_best_move
3. cli_ui.py - Should contain UI-related functions
4. main.py - The entry point

You want to create a new file for game-related functions that aren't part of game_tree.py.

Let's organize content for these files:

### For cli_ui.py (UI-related functions)
This should contain all the user interface functions:

```python
# cli_ui.py

def display_game_tree_header():
    print("Spēles koks:")

def get_algorithm_choice():
    print("\nIzvēlies algoritmu:")
    print("1 - Alpha-Beta")
    print("2 - Minimax")
    algorithm_choice = input("Ievadi 1 vai 2: ").strip()
    
    use_alpha_beta = algorithm_choice == "1"
    use_minimax = algorithm_choice == "2"
    
    return use_alpha_beta, use_minimax

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
```

### For a new file - game_logic.py (Game-related functions)
This will contain game flow, player handling, etc.:

```python
# game_logic.py
from game_tree import GameState, print_game_tree
from algoritmi import get_best_move
import cli_ui

def process_human_turn(current_state):
    """Handle human player's turn"""
    multiplier = cli_ui.get_human_move()
    
    # Apply human move
    next_states = current_state.generate_next_states()
    new_state = None
    
    for state in next_states:
        if state.number == current_state.number * multiplier:
            new_state = state
            break
    
    cli_ui.display_human_move(new_state, multiplier)
    return new_state

def process_ai_turn(current_state, max_depth, use_minimax, use_alpha_beta):
    """Handle AI player's turn"""
    cli_ui.prompt_for_ai_move()
    
    best_move = get_best_move(
        current_state, 
        max_depth, 
        use_minimax=use_minimax, 
        use_alpha_beta=use_alpha_beta
    )
    
    if best_move is None:
        print("\nSpēle beigusies!")
        return None
    
    ai_multiplier = best_move.number // current_state.number
    cli_ui.display_ai_move(best_move, ai_multiplier)
    
    return best_move

def initialize_game():
    """Initialize the game state and settings"""
    initial_state = GameState(number=5)
    max_depth = 7
    
    # Display game tree
    cli_ui.display_game_tree_header()
    print_game_tree(initial_state, max_depth)
    
    # Get algorithm choice
    use_alpha_beta, use_minimax = cli_ui.get_algorithm_choice()
    
    # Display initial state
    cli_ui.display_initial_state(initial_state)
    
    return initial_state, max_depth, use_alpha_beta, use_minimax

def run_game_loop(initial_state, max_depth, use_alpha_beta, use_minimax):
    """Run the main game loop"""
    current_state = initial_state
    
    while current_state.number < 1000:
        if current_state.is_human_turn:
            # Human's turn
            current_state = process_human_turn(current_state)
        else:
            # AI's turn
            new_state = process_ai_turn(
                current_state, 
                max_depth, 
                use_minimax, 
                use_alpha_beta
            )
            
            if new_state is None:
                break
                
            current_state = new_state
    
    cli_ui.display_game_end(current_state)
```

### For main.py (Entry point)
This should be simple and just run the game:

```python
# main.py
from game_logic import initialize_game, run_game_loop

def main():
    # Initialize game
    initial_state, max_depth, use_alpha_beta, use_minimax = initialize_game()
    
    # Run game loop
    run_game_loop(
        initial_state,
        max_depth,
        use_alpha_beta,
        use_minimax
    )

if __name__ == "__main__":
    main()
```

These files maintain a clear separation of concerns:
1. game_tree.py - Game state and tree structure (already exists)
2. algoritmi.py - AI algorithms for game decision making (already exists)
3. cli_ui.py - User interface functions for interaction and display
4. game_logic.py - Game flow and player actions 
5. main.py - Entry point that ties everything together

This structure keeps related functionalities together while separating them into logical groups.
# Project File Structure

Based on your existing files and requirements, here's a new game-related file to add to your project structure:

## game_logic.py
This will contain all the game-related functions separate from game_tree.py and user interface code:

```python
# game_logic.py
from game_tree import GameState, print_game_tree
from algoritmi import get_best_move
import cli_ui

def process_human_turn(current_state):
    """Handle human player's turn"""
    multiplier = cli_ui.get_human_move()
    
    # Apply human move
    next_states = current_state.generate_next_states()
    new_state = None
    
    for state in next_states:
        if state.number == current_state.number * multiplier:
            new_state = state
            break
    
    cli_ui.display_human_move(new_state, multiplier)
    return new_state

def process_ai_turn(current_state, max_depth, use_minimax, use_alpha_beta):
    """Handle AI player's turn"""
    cli_ui.prompt_for_ai_move()
    
    best_move = get_best_move(
        current_state, 
        max_depth, 
        use_minimax=use_minimax, 
        use_alpha_beta=use_alpha_beta
    )
    
    if best_move is None:
        print("\nSpēle beigusies!")
        return None
    
    ai_multiplier = best_move.number // current_state.number
    cli_ui.display_ai_move(best_move, ai_multiplier)
    
    return best_move

def initialize_game():
    """Initialize the game state and settings"""
    initial_state = GameState(number=5)
    max_depth = 7
    
    # Display game tree
    cli_ui.display_game_tree_header()
    print_game_tree(initial_state, max_depth)
    
    # Get algorithm choice
    use_alpha_beta, use_minimax = cli_ui.get_algorithm_choice()
    
    # Display initial state
    cli_ui.display_initial_state(initial_state)
    
    return initial_state, max_depth, use_alpha_beta, use_minimax

def run_game_loop(initial_state, max_depth, use_alpha_beta, use_minimax):
    """Run the main game loop"""
    current_state = initial_state
    
    while current_state.number < 1000:
        if current_state.is_human_turn:
            # Human's turn
            current_state = process_human_turn(current_state)
        else:
            # AI's turn
            new_state = process_ai_turn(
                current_state, 
                max_depth, 
                use_minimax, 
                use_alpha_beta
            )
            
            if new_state is None:
                break
                
            current_state = new_state
    
    cli_ui.display_game_end(current_state)
```

## Update cli_ui.py
Ensure your cli_ui.py file contains all the necessary UI functions:

```python
# cli_ui.py

def display_game_tree_header():
    print("Spēles koks:")

def get_algorithm_choice():
    print("\nIzvēlies algoritmu:")
    print("1 - Alpha-Beta")
    print("2 - Minimax")
    algorithm_choice = input("Ievadi 1 vai 2: ").strip()
    
    use_alpha_beta = algorithm_choice == "1"
    use_minimax = algorithm_choice == "2"
    
    return use_alpha_beta, use_minimax

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
```

## Update main.py
Simplify your main.py to use the new functions:

```python
# main.py
from game_logic import initialize_game, run_game_loop

def main():
    # Initialize game
    initial_state, max_depth, use_alpha_beta, use_minimax = initialize_game()
    
    # Run game loop
    run_game_loop(
        initial_state,
        max_depth,
        use_alpha_beta,
        use_minimax
    )

if __name__ == "__main__":
    main()
```

## Final Project Structure
- **game_tree.py** - Contains GameState class and print_game_tree (existing)
- **algoritmi.py** - Contains AI algorithms like get_best_move (existing)
- **cli_ui.py** - Contains all UI-related functions
- **game_logic.py** - Contains game flow and player actions (new)
- **main.py** - Simple entry point

This structure keeps related functionality together while maintaining a clear separation between game state, game flow, user interface, and AI algorithms.