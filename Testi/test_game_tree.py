from game.game_state import GameState
from game.game_tree import GameTree

def get_int_input(prompt, min_value=None, max_value=None):
    """Helper function to get integer input with validation"""
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Value must be at most {max_value}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")

def get_yes_no_input(prompt):
    """Helper function to get yes/no input"""
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please answer with yes (y) or no (n).")

def modify_game_state_class(terminal_score):
    """Modifies the GameState class to use the user-defined terminal score"""
    # This is a monkey patch for the is_terminal method
    original_is_terminal = GameState.is_terminal
    
    def new_is_terminal(self):
        """
        Modified terminal check with user-defined threshold.
        """
        return self.current_number >= terminal_score
    
    GameState.is_terminal = new_is_terminal
    return original_is_terminal

def run_game_tree_cli():
    """Main function for the CLI application"""
    print("=" * 50)
    print("Welcome to Game Tree Explorer".center(50))
    print("=" * 50)
    
    # Get initial game number
    initial_number = get_int_input("Enter the initial game number: ", min_value=1)
    
    # Get terminal score threshold
    terminal_score = get_int_input("Enter the terminal score threshold: ", min_value=10)
    
    # Modify the GameState class
    original_is_terminal = modify_game_state_class(terminal_score)
    
    # Determine who starts
    computer_starts = get_yes_no_input("Should the computer make the first move? (y/n): ")
    
    # Create initial game state
    if computer_starts:
        initial_state = GameState(initial_number, True)
        print(f"Creating game with initial number {initial_number} (Computer starts)")
    else:
        initial_state = GameState(initial_number)
        print(f"Creating game with initial number {initial_number} (Player starts)")
    
    # Get exploration depth
    exploration_depth = get_int_input("Enter the exploration depth: ", min_value=1, max_value=10)
    
    # Create and expand the game tree
    print("\nCreating game tree...")
    tree = GameTree(initial_state)
    
    print(f"Expanding tree to depth {exploration_depth}...")
    tree.expand_node(tree.root, exploration_depth)
    
    # Display results
    print(f"\nTree expansion complete.")
    print(f"Terminal score threshold: {terminal_score}")
    print(f"Total number of nodes: {tree.get_nodes_count()}")
    
    # Ask user if they want to see the tree structure
    if get_yes_no_input("\nDo you want to see the tree structure? (y/n): "):
        print("\nTree structure:")
        tree.print_tree()
    
    # Ask user if they want to run another analysis
    if get_yes_no_input("\nDo you want to run another analysis? (y/n): "):
        # Restore original is_terminal method
        GameState.is_terminal = original_is_terminal
        run_game_tree_cli()
    else:
        # Restore original is_terminal method before exiting
        GameState.is_terminal = original_is_terminal
        print("\nThank you for using Game Tree Explorer!")

if __name__ == "__main__":
    run_game_tree_cli()