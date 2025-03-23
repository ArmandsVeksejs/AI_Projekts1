def evaluate(state):
    # aprēķinām punktu starpību
    score_difference = state.computer_points - state.human_points 
    # atrast pašreizējo gājiena numuru, dalot ar 10, var samazināt šī skaitļa ietekmi
    number_factor = state.current_number / 10

    # tiek atgriezta fiksēta vērtība: 10000 - ja dators uzvarēja, -10000 - ja uzvarējis cilvēks -- Šī vērtība norāda spēles beigas
    if state.is_game_over:
        return 10000 if state.computer_points > state.human_points else -10000

    # Šī summa būs pašreizējā spēles stāvokļa novērtējums, lai pieņemtu lēmumus spēles stratēģijā (piemēram, minimax meklēšanas algoritma gadījumā)
    return score_difference + number_factor