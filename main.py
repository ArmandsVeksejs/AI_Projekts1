import tkinter as tk
from game import GameState, print_game_tree
from gui import GUI

def main():

    """ Ja grib palaist CLI print tree """
    # initial_state = GameState(number=7)
    # max_depth = 3
    # print("Spēles koks:")
    # print_game_tree(initial_state, max_depth)

    """Ja grib palaist GUI"""
    root = tk.Tk()
    app = GUI (root)
    root.mainloop()

if __name__ == "__main__":
    main()