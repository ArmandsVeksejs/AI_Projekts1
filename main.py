from game import GameState, print_game_tree
from algoritmi import get_best_move, heuristic

def main():

    initial_state = GameState(number=7)
    max_depth = 3
    current_state = initial_state

    print("Spēles koks:")
    print_game_tree(initial_state, max_depth)

    print("\nIzvēlies algoritmu:")
    print("1 - Alpha-Beta")
    print("2 - Minimax")
    algoritm_choice = input("Ievadi 1 vai 2: ").strip()

    use_alpha_beta = algoritm_choice == "1"
    use_minimax = algoritm_choice == "2"

    while current_state.number < 1000:
        input("\nVai vēlies redzēt nākamo move? (spied Enter, lai turpinātu) ")

        best_move = get_best_move(current_state, max_depth, use_minimax=use_minimax, use_alpha_beta=use_alpha_beta)

        if best_move is None:
            print("\nSpēle beigusies!")
            break

        print(f"\nLabākais gājiens: {best_move}")
        current_state = best_move

    print("\nSpēle beigusies!")

if __name__ == "__main__":
    main()