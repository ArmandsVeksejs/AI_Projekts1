from game import GameState, print_game_tree

def main():
    initial_state = GameState(number=7)
    max_depth = 3
    print("Spēles koks:")
    print_game_tree(initial_state, max_depth)

if __name__ == "__main__":
    main()