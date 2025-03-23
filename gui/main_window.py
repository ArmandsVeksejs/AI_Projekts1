import tkinter as tk
from game.game_engine import GameEngine

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Spēle")
        self.root.geometry("800x600")
        
        self.game_engine = None
        self.create_setup_panel()
    
    def create_setup_panel(self):
        """
        Spēles sākuma logs, prasa lietotājam ievadīt spēles sākuma parametrus.
        """
        self.setup_frame = tk.Frame(self.root, padx=20, pady=20)
        self.setup_frame.pack(expand=True)

        self.create_description()
        self.create_number_selection()
        self.create_player_selection()
    
    def create_description(self):
        """
        Spēles apraksts.
        """
        title_label = tk.Label(self.setup_frame, text="Skaitļu reizināšanas spēle", font=("Arial", 18, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        description_label = tk.Label(
            self.setup_frame, 
            text="Spēles sākumā ir dots cilvēka-spēlētāja izvēlētais skaitlis. Abiem spēlētājiem ir 0 punktu. "
                "Spēlētāji veic gājienus pēc kārtas, reizinot pašreizējā brīdī esošu skaitli ar 2 vai 3. "
                "Ja reizināšanas rezultātā tiek iegūts pāra skaitlis, tad spēlētāja punktu skaitam tiek pieskaitīts 1 punkts, "
                "bet ja nepāra skaitlis, tad 1 punkts tiek atņemts. Spēle beidzas, kā tikko ir iegūts skaitlis, kas ir lielāks "
                "vai vienāds ar 1000. Spēlētājs ar mazāko punktu skaitu uzvar spēli. Ja punktu skaits ir vienāds, tad rezultāts "
                "ir neizšķirts. Papildu prasības programmatūrai: Spēles sākumā cilvēks-spēlētājs izvēlas, ar kuru skaitli diapazonā "
                "no 5 līdz 15 sākt spēli.",
            font=("Arial", 12),
            wraplength=600,
            justify="center"
        )
        description_label.grid(row=1, column=0, columnspan=2, pady=(0, 15))

    def create_number_selection(self):
        """
        Prasa cilvēkam izvēlēties spēles sākuma skaitli.
        """
        number_label = tk.Label(self.setup_frame, text="Izvēlies skaitli (5-15):")
        number_label.grid(row=2, column=0, sticky="w", pady=5)
        self.number_scale = tk.Scale(self.setup_frame, from_=5, to=15, orient=tk.HORIZONTAL, length=200)
        self.number_scale.grid(row=2, column=1, pady=5, padx=10, sticky="ew")

    def create_player_selection(self):
        """
        Parāda spēlētāju opcijas.
        """
        player_label = tk.Label(self.setup_frame, text="Kurš sāk spēli:")
        player_label.grid(row=3, column=0, sticky="w", pady=5)
        self.first_player_var = tk.StringVar(value="cilvēks")
        player_options = ["cilvēks", "dators"]
        player_dropdown = tk.OptionMenu(self.setup_frame, self.first_player_var, *player_options)
        player_dropdown.grid(row=3, column=1, sticky="ew", pady=5, padx=10)
        player_dropdown.config(width=15)

    #TODO
    def create_algorithm_selection(self):
        pass

    #TODO
    def create_start_button(self):
        pass
    
    def start_game(self):
        """
        Palaiž spēli. No sākuma tiek izveidots logs, kurā cilvēks norāda spēles parametrus (skaitli, kas sāk, kurš algoritms)
        """
        starting_number = self.number_scale.get()
        first_player = self.first_player_var.get()
        self.game_engine = GameEngine(starting_number, first_player)

        self.setup_frame.destroy()
        # self.create_game_interface()