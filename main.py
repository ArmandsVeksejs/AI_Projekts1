from game import GameState, print_game_tree
from algoritmi import get_best_move,heuristic

def main():

    
    initial_state = GameState(number=7)
    max_depth = 3

    print("Spēles koks:")
    print_game_tree(initial_state, max_depth)
    
    best_move = get_best_move(initial_state, max_depth)
    print("\nLabākais gājiens, ko izvēlas AI (ar alpha-beta):")
    #Vai cilvēka gājiens=False (tas nozime ka šis gājiens noved pie AI priekšrocības nākotnē)
    print(best_move)

if __name__ == "__main__":
    main()