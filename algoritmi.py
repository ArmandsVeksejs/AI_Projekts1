from game import GameState

MAX, MIN = 1000, -1000

def alpha_beta(depth, state: GameState, maximizing_player: bool, alpha, beta):
    # Pārbaude – vai sasniegts spēles beigu stāvoklis
    if state.number >= 1000 or depth == 0:
        return heuristic(state)

    # MAX spēlētājs (AI)
    if maximizing_player:
        best = MIN
        #Iegūstam visus nākamos iespējamos stāvokļus, reizinot ar 2 vai 3
        for child in state.generate_next_states():
            #rekurzīvi dodamies uz bērnu virsotni,ejot 1 līmeni dziļāk,Nākamais gājiens būs cilvēkam (MIN), tāpēc False
            child_score = alpha_beta(depth - 1, child, False, alpha, beta)
            #AI izvelas maksimālo no visiem child_score
            best = max(best, child_score)
            #labākais, ko līdz šim atradis MAX spēlētājs
            alpha = max(alpha, best)
            #konflikta pārbaude
            if beta <= alpha:
                break
        return best

    #MIN spēlētājs (Cilvēks)
    else:
        best = MAX
        for child in state.generate_next_states():
            child_score = alpha_beta(depth - 1, child, True, alpha, beta)
            best = min(best,child_score)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

def minimax():
    pass

def heuristic(self):
    # Mērķis - mazāks punktu skaits nekā pretiniekam
    # Viss, kas tiecas pretī šim mērķim dod pozitīvu vērtību
    # Pretinieks - spēlētājs, kurš nesāka spēli
    score_difference = self.ai_score - self.human_score

    # Izveido vērtību no 0 līdz 1, kas norāda, cik tuvu mēs esam spēles beigu stāvoklim (1000).
    # Spēle tiek sadalīta fāzēs, pamatojoties uz pašreizējo skaitli.
    proximity_to_end = min(1.0, self.number / 500)
    # Kad skaitlis = 50: proximity_to_end = 0,1 (10% no 500)
    # Kad skaitlis = 250: proximity_to_end = 0,5 (50% no 500)
    # Ja skaits = 500 vai lielāks: proximity_to_end = 1,0 (sasniegta maksimālā ietekme, jo nākamajā gājienā spēle beigsies.

    # Nepāra skaitļi ir stratēģiski ļoti vērtīgi it īpaši spēles sākumā, jo:
    # Nepāra skaitlis × 3 = vēl viens nepāra skaitlis
    # Ar nepāra skaitļiem var vienmēr zaudēt punktus.
    # Spēlētājam, kurš pirmais iegūst nepāra skaitli, ir priekšrocība, ja to iegūst jau uzreiz spēles sākumā, tad zaudēt nav iespējams.
    parity_advantage = 0
    if self.number % 2 == 1:
        if self.is_human_turn:
            parity_advantage = 0.7
        else:
            parity_advantage = -0.7  # SLIKTI! AI var izmantot nepāra skaitli lai samazinātu sev rezultātu

    # Pāra skaitļi ir slikti, jo:
    # Abas reizināšanas iespējas (×2 un ×3) dod pāra skaitļus.
    # Pāra skaitļi vienmēr dod +1 punktu (šajā spēlē tas ir slikti).
    # Nākamais spēlētājs tiek “iesprostots”, punktu palielināšanā.
    future_options = 0
    if self.number % 2 == 0:  # AI tiks spiests iegūt +1 punktu nākamajā gājienā.
        if self.is_human_turn:  # LABI! AI būs spiests saņemt +1 punktu nākamajā gājienā
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

def get_best_move(state: GameState, depth: int):
    best_child_score = MIN
    best_state = None
    for child in state.generate_next_states():
        move_child_score = alpha_beta(depth - 1, child, False, MIN, MAX)
        if move_child_score > best_child_score:
            best_child_score = move_child_score
            best_state = child
    return best_state