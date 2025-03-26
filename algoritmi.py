from game import GameState

MAX, MIN = 1000, -1000

def alpha_beta(depth, state: GameState, maximizing_player: bool, alpha, beta):
    if state.number >= 1000 or depth == 0:
        return heuristic(state)

    if maximizing_player:
        best = MIN
        for child in state.generate_next_states():
            child_score = alpha_beta(depth - 1, child, False, alpha, beta)
            best = max(best, child_score)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best

    else:
        best = MAX
        for child in state.generate_next_states():
            child_score = alpha_beta(depth - 1, child, True, alpha, beta)
            best = min(best,child_score)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best


def minimax(depth, state: GameState, maximiziting_player: bool):
    if state.number >= 1000 or depth == 0:
        return heuristic(state), None
    
    best_move = None

    if maximiziting_player:
        best = MIN
        for child in state.generate_next_states():
            child_score, _ = minimax(depth - 1, child, False)
            if child_score > best:
                best = child_score
                best_move = child
        return best, best_move
        
    else:
        best = MAX
        for child in state.generate_next_states():
            child_score, _ = minimax(depth - 1, child, True)
            if child_score < best:
                best = child_score
                best_move = child
        return best, best_move

def heuristic(self):
    score_difference = self.ai_score - self.human_score
    proximity_to_end = min(1.0, self.number / 500)
    parity_advantage = 0
    if self.number % 2 == 1:
        if self.is_human_turn:
            parity_advantage = 0.7
        else:
            parity_advantage = -0.7
    future_options = 0
    if self.number % 2 == 0:
        if self.is_human_turn:
            future_options = 0.5
        else:
            future_options = -0.5

    immediate_value = score_difference * (0.5 + 0.5 * proximity_to_end)
    strategic_value = (parity_advantage + future_options) * (1 - 0.5 * proximity_to_end)
    return immediate_value + strategic_value

def get_best_move(state: GameState, depth: int, use_minimax: bool, use_alpha_beta: bool):
    best_child_score = MIN
    best_state = None
    for child in state.generate_next_states():
        if use_alpha_beta:
            move_child_score = alpha_beta(depth - 1, child, False, MIN, MAX)
        elif use_minimax:
            move_child_score, _ = minimax(depth - 1, child, False)
        else:
            raise ValueError("Neizvēlēts algoritms!")
        
        if move_child_score > best_child_score:
            best_child_score = move_child_score
            best_state = child
    return best_state