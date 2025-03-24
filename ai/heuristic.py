import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) #vajadzigs lai atrast game.game_state(izmantoju chatgpt)
# Chata paskaidrojums "Šis nodrošina, ka ai/heuristic.py var atrast moduli game.game_state, jo Python ceļš tiek papildināts ar projekta sakni."
from game.game_state import GameState

def heuristic(state):
    # Ja spele ir beigusies, atgriež galeju vertibu atkarība no ta, kurš uzvareja
    if state.is_game_over:
        if state.human_points < state.computer_points:
            return float('inf')  # Cilveks uzvarejis
        elif state.human_points > state.computer_points:
            return float('-inf')  # Dators uzvarejis
        else:
            return 0  # Neizšķirts

    # Preteja starpiba, jo mazaks punktu skaits ir labak
    # Ja spele vel nav gala, noverte punktu starpibu
    #Ja pozitiva cilveks labaka pozicija.
    #Ja negativa dators labaka pozicija.
    return state.computer_points - state.human_points 

#Tests/Piemers lai redzetu ka tas stradas un kads bus rezultats
#So koda bloku vares pec tam nokomentet
if __name__ == "__main__":
    # Sākuma skaitlis 10, cilvēks 1 punkts, dators 3 punkti
    start = GameState(10)
    start.human_points = 1
    start.computer_points = 3

    print("Heuristikas rezultāts:", heuristic(start)) #Rezultāts: 2 tad cilvēkam labāka pozīcija (sakuma)
