from game_tree import GameState
import algoritmi
import cli_ui

def initialize_game():
    initial_state = GameState(number=5, is_human_turn=False)
    max_depth = 7
    
    # cli_ui.display_game_tree(initial_state, max_depth)
    # Atkomentēt, ja gribat redzēt pilno spēles koku
    
    use_alpha_beta, use_minimax = cli_ui.get_algorithm_choice()
    
    cli_ui.display_initial_state(initial_state)
    
    return initial_state, max_depth, use_alpha_beta, use_minimax

def run_game_loop(initial_state, max_depth, use_alpha_beta, use_minimax):
    current_state = initial_state
    
    while current_state.number < 1000:
        if current_state.is_human_turn:
            current_state = process_human_turn(current_state)
        else:
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

def process_human_turn(current_state):
    multiplier = cli_ui.get_human_move()
    
    new_number = current_state.number * multiplier
    # Skaitlis var būt arī > 1000 – cilvēkam atļauts
    new_human_score, new_ai_score = current_state.calculate_scores(new_number)

    new_state = GameState(
        new_number,
        human_score=new_human_score,
        ai_score=new_ai_score,
        depth=current_state.depth + 1,
        is_human_turn=False,  # pēc cilvēka nāk AI
        parent=current_state
    )

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

    for child in sorted(state.generate_next_states(raw=True), key=lambda x: x.number):
        if use_alpha_beta:
            move_child_score = algoritmi.alpha_beta(depth - 1, child, False, algoritmi.MIN, algoritmi.MAX)
        elif use_minimax:
            move_child_score, _ = algoritmi.minimax(depth - 1, child, False)
        else:
            raise ValueError("Kļūda! Ievadi 2 vai 3!!!")

        # Atļaujam gājienus >1000 TIKAI, ja tie dod uzvaru
        if child.number > 1000:
            if child.ai_score < child.human_score:
                if move_child_score > best_child_score or best_state is None:
                    best_child_score = move_child_score
                    best_state = child
        else:
            if move_child_score > best_child_score or best_state is None:
                best_child_score = move_child_score
                best_state = child

    return best_state