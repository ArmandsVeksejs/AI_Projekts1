from game_logic import initialize_game, run_game_loop
import tkinter as tk
from GUI import gui

def main():
    # initial_state, max_depth, use_alpha_beta, use_minimax = initialize_game()
    #
    # run_game_loop(
    #     initial_state,
    #     max_depth,
    #     use_alpha_beta,
    #     use_minimax
    # )
    
    root = tk.Tk()
    app = gui(root)
    root.mainloop()

if __name__ == "__main__":
    main()