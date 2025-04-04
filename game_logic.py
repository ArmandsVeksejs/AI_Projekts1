from game_tree import GameState
import algoritmi
import cli_ui
import time

def initialize_game():
    initial_number = cli_ui.get_starting_number()
    is_human_turn = cli_ui.get_starting_player()
    initial_state = GameState(number=initial_number, is_human_turn=is_human_turn)
    max_depth = 4
    
    # Comment/uncomment as needed to show game tree in the shell
    # cli_ui.display_game_tree(initial_state, max_depth)
    
    use_alpha_beta, use_minimax = cli_ui.get_algorithm_choice()
    
    cli_ui.display_initial_state(initial_state)

    algoritmi.reset_nodes_visited()
    
    return initial_state, max_depth, use_alpha_beta, use_minimax

def run_game_loop(initial_state, max_depth, use_alpha_beta, use_minimax):
    current_state = initial_state
    total_ai_time = 0
    ai_moves = 0
    total_nodes_visited = 0
    
    while current_state.number < 1000:
        if current_state.is_human_turn:
            current_state = process_human_turn(current_state)
        else:
            algoritmi.reset_nodes_visited()
            
            start_time = time.time()
            
            new_state = process_ai_turn(
                current_state, 
                max_depth, 
                use_minimax, 
                use_alpha_beta
            )
            
            if new_state is None:
                break
            
            end_time = time.time()
            full_turn_time = end_time - start_time
            
            nodes_visited = algoritmi.get_nodes_visited()
            total_nodes_visited += nodes_visited
            
            total_ai_time += full_turn_time
            ai_moves += 1
                
            current_state = new_state
    
    cli_ui.display_game_end(current_state)
    
    print(f"\nVidējais datora gājiena laiks: {total_ai_time / ai_moves:.6f} sekundes")
    print(f"Kopējais apmeklēto virsotņu skaits: {total_nodes_visited}")

def process_human_turn(current_state):
    multiplier = cli_ui.get_human_move()
    
    new_state = current_state.generate_next_state(multiplier)
    
    cli_ui.display_human_move(new_state, multiplier)
    return new_state

def process_ai_turn(current_state, max_depth, use_minimax, use_alpha_beta):
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

def get_best_move(state: GameState, depth: int, use_minimax: bool, use_alpha_beta: bool):
    best_child_score = algoritmi.MIN
    best_state = None
    for child in state.generate_next_states():
        if use_alpha_beta:
            move_child_score = algoritmi.alpha_beta(depth - 1, child, True, algoritmi.MIN, algoritmi.MAX)
        elif use_minimax:
            move_child_score, _ = algoritmi.minimax(depth - 1, child, True)
        else:
            raise ValueError("Kļūda! Ievadi 2 vai 3!!!")

        if move_child_score > best_child_score:
            best_child_score = move_child_score
            best_state = child
    return best_state