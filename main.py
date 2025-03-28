"""
Šī ir programma, kas īsteno sekojošās spēles analīzi:

Spēles apraksts:
    Spēles sākumā ir dots cilvēka-spēlētāja izvēlētais skaitlis. Abiem spēlētājiem ir 0 punktu. Spēlētāji veic gājienus pēc kārtas, reizinot pašreizējā brīdī esošu skaitli ar 2 vai 3. Ja reizināšanas rezultātā tiek iegūts pāra skaitlis, tad spēlētāja punktu skaitam tiek pieskaitīts 1 punkts, bet ja nepāra skaitlis, tad 1 punkts tiek atņemts. Spēle beidzas, kā tikko ir iegūts skaitlis, kas ir lielāks vai vienāds ar 1000. Spēlētājs ar mazāko punktu skaitu uzvar spēli. Ja punktu skaits ir vienāds, tad rezultāts ir neizšķirts.

Papildu prasības programmatūrai:
    Spēles sākumā cilvēks-spēlētājs izvēlas, ar kuru skaitli diapazonā no 5 līdz 15 sākt spēli. 
"""

import tkinter as tk
from game import GameEngine
from GUI import GUI

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