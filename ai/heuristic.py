def evaluate(state):
    """
    jauna heuristika funkcija
    
    argumenti:
        state (GameState) - pašreizejaus speles stavoklis
        
    atgriež:
        float - stavokļa novertejums (jo augstak vertejums, jo labak datoram)
    """
    
    # ja spele ir beigusies, atgriež maksimalo vai minimalo vertibu
    if state.is_game_over:
        if state.computer_points < state.human_points:
            return float('inf') # dators uzvareja (jo vinam ir LESS punktu)
        elif state.computer_points > state.human_points:
            return float('-inf') # cilveks uzvareja (jo ir MORE punktu)
        else:
            return 0 # neizšķirts
        
    # punktu starpiba (neliels koef. jo starpiba iz maza)    
    score_diff = (state.computer_points - state.human_points)*2
    
    # speles progresa indikators (ka strauji pieaug skaitlis)
    game_progress = state.current_number / 1000
    
    # nakamo iespejamo gajienu analize
    next_moves = [state.current_number * 2, state.current_number * 3]
    safe_moves = sum(1 for move in next_moves if move < 1000)
    
    # parbaude vai kads no nakošiem gajieniem uzreiz dod uzvaru
    immediate_win = any(move == 1000 for move in next_moves)
    
    # soda punkti par tuvinašanos pie 1000 lai izvairities no atras speles beigam
    risk_penalty = -50 if state.current_number > 900 else 0
    
    # bonuss datoram ja punktu skaits ir ieverojami lielaks par cilveka punktu skaitu
    domination_bonus = 30 if score_diff > 2 else 0
    
    # gala novertejums
    return(
        score_diff + (5 * game_progress) + (10 * safe_moves) + 
        (100 * immediate_win) + risk_penalty + domination_bonus)