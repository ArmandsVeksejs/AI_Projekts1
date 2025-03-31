from game_tree import GameState

MAX, MIN = 1000, -1000
nodes_visited = 0

def reset_nodes_visited():
    global nodes_visited
    nodes_visited = 0

def get_nodes_visited():
    global nodes_visited
    return nodes_visited

def minimax(depth, state: GameState, maximizing_player: bool):
    global nodes_visited
    nodes_visited += 1
    
    if state.number >= 1000 or depth == 0:
        return heuristic(state), None

    best_move = None

    if maximizing_player:
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

def alpha_beta(depth, state: GameState, maximizing_player: bool, alpha, beta):
    global nodes_visited
    nodes_visited += 1
    
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

def heuristic(state):
    score_diff = state.human_score - state.ai_score
    return score_diff