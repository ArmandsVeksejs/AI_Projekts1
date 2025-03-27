from game_logic import initialize_game, run_game_loop

def main():
    initial_state, max_depth, use_alpha_beta, use_minimax = initialize_game()
    
    run_game_loop(
        initial_state,
        max_depth,
        use_alpha_beta,
        use_minimax
    )

if __name__ == "__main__":
    main()