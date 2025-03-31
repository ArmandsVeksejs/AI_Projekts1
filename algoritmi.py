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
    # Mērķis - mazāks punktu skaits nekā pretiniekam
    # Viss, kas tiecas pretī šim mērķim dod pozitīvu vērtību
    # Pretinieks - spēlētājs, kurš nesāka spēli
    score_difference = state.human_score - state.ai_score

    # Izveido vērtību no 0 līdz 1, kas norāda, cik tuvu mēs esam spēles beigu stāvoklim (1000).
    # Spēle tiek sadalīta fāzēs, pamatojoties uz pašreizējo skaitli.
    proximity_to_end = min(1.0, state.number / 500)
    # Kad skaitlis = 50: proximity_to_end = 0,1 (10% no 500)
    # Kad skaitlis = 250: proximity_to_end = 0,5 (50% no 500)
    # Ja skaitlis = 500 vai lielāks: proximity_to_end = 1,0 (sasniegta maksimālā ietekme, jo nākamajā gājienā spēle beigsies.

    # Nepāra skaitļi ir stratēģiski ļoti vērtīgi it īpaši spēles sākumā, jo:
    # Nepāra skaitlis × 3 = vēl viens nepāra skaitlis
    # Ar nepāra skaitļiem var vienmēr zaudēt punktus.
    # Spēlētājam, kurš pirmais iegūst nepāra skaitli, ir priekšrocība, ja to iegūst jau uzreiz spēles sākumā, tad zaudēt nav iespējams.
    parity_advantage = 0
    if state.number % 2 == 1:
        if state.is_human_turn:
            parity_advantage = 0.7
        else:
            parity_advantage = -0.7  # SLIKTI! AI var izmantot nepāra skaitli lai samazinātu sev rezultātu

    # Pāra skaitļi ir slikti, jo:
    # Abas reizināšanas iespējas (×2 un ×3) dod pāra skaitļus.
    # Pāra skaitļi vienmēr dod +1 punktu (šajā spēlē tas ir slikti).
    # Nākamais spēlētājs tiek “iesprostots”, punktu palielināšanā.
    future_options = 0
    if state.number % 2 == 0:  # AI tiks spiests iegūt +1 punktu nākamajā gājienā.
        if state.is_human_turn:  # LABI! AI būs spiests saņemt +1 punktu nākamajā gājienā
            future_options = 0.5
        else:  # SLIKTI! Cilvēks būs spiests saņemt +1 punktu nakamajā gājienā
            future_options = -0.5

    # Spēlei tuvojieties beigām 
    immediate_value = score_difference * (0.5 + 0.5 * proximity_to_end)
    # Spēles sākumā (skaitlis = 50, tuvums = 0,1): Svars = 0,5 + 0,5 × 0,1 = 0,55
    # Spēles beigās (skaitlis = 450, tuvums = 0,9): Svars = 0,5 + 0,5 × 0,9 = 0,95
    # Punktu starpība kļūst gandrīz pilnībā noteicošā.

    strategic_value = (parity_advantage + future_options) * (1 - 0.5 * proximity_to_end)
    # Spēles sākumā (skaitlis = 50, tuvums = 0,1): Svars = 1 - 0,5 × 0,1 = 0,95. Stratēģiskie faktori ir ļoti nozīmīgi. Piemēram ja varam iegūt nepāra skaitli jau uzreiz, garantēts, ka uzvarēsim vai būs neizšķirts.
    # Spēles beigās (skaitlis = 450, tuvums = 0,9): Svars = 1 - 0,5 × 0,9 = 0,55. Stratēģiskie faktori kļūst mazāk nozīmīgi.

    # Apvieno gan immediate gan strategic faktorus.
    return immediate_value + strategic_value