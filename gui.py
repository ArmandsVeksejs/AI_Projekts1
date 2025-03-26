import tkinter as tk
from tkinter import messagebox
from game import GameState

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Spēle")
        self.root.geometry("800x600")
        # self.game_engine = None
        self.create_setup_panel()

    # Sākuma logs
    def create_setup_panel(self):
        self.setup_frame = tk.Frame(self.root, padx=20, pady=20)
        self.setup_frame.pack(expand=True)
        self.create_title()
        self.create_description()
        self.create_number_selection()
        self.create_player_selection()
        self.create_algorithm_selection()
        self.create_start_button()
        self.create_autoplay_button()
        self.create_exit_button()

    # Row 1
    def create_title(self):
        title_label = tk.Label(
            self.setup_frame, 
            text="Skaitļu reizināšanas spēle", 
            font=("Arial", 18, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    # Row 2
    def create_description(self):
        description_text = tk.Text(
            self.setup_frame,
            height=8,
            width=70,
            wrap=tk.WORD,
            padx=10,
            pady=10,
            relief=tk.FLAT,
            background=self.setup_frame.cget('background')
        )
    
        description_text.insert(tk.END, 
            "Abiem spēlētājiem ir 0 punktu. Spēlētāji veic gājienus pēc kārtas, "
            "reizinot pašreizējā brīdī esošu skaitni ar 2 vai 3.\n\n"
            
            "Ja reizināšanas rezultātā tiek iegūts pāra skaitlis, tad spēlētāja "
            "punktu skaitam tiek pieskaitīts 1 punkts, bet ja nepāra skaitlis, "
            "tad 1 punkts tiek atņemts.\n\n"
            
            "Spēle beidzas, kā tikko ir iegūts skaitlis, kas ir lielāks vai "
            "vienāds ar 1000. Spēlētājs ar mazāko punktu skaitu uzvar spēli. "
            "Ja punktu skaits ir vienāds, tad rezultāts ir neizšķirts.\n\n"
        )

        description_text.configure(state='disabled')
        description_text.grid(row=1, column=0, columnspan=2, pady=(0, 15))

    # Row 3
    def create_number_selection(self):
        self.create_number_label()
        self.create_number_scale()

    def create_number_label(self):
        number_label = tk.Label(self.setup_frame, text="Izvēlies skaitli (5-15):")
        number_label.grid(row=2, column=0, sticky="w", pady=5)

    def create_number_scale(self):
        self.number_scale = tk.Scale(self.setup_frame,from_=5,to=15,orient=tk.HORIZONTAL,length=200)
        self.number_scale.grid(row=2,column=1,pady=5,padx=10,sticky="ew")

    # Row 4
    def create_player_selection(self):
        self.create_player_label()
        self.create_player_dropdown()

    def create_player_label(self):
        player_label = tk.Label(self.setup_frame, text="Kurš sāk spēli:")
        player_label.grid(row=3, column=0, sticky="w", pady=5)

    def create_player_dropdown(self):
        self.first_player_var = tk.StringVar(value="cilvēks")
        player_dropdown = tk.OptionMenu(self.setup_frame, self.first_player_var, "cilvēks", "dators")
        player_dropdown.grid(row=3, column=1, sticky="ew", pady=5, padx=10)
        player_dropdown.config(width=15)

    # Row 5
    def create_algorithm_selection(self):
        self.create_algorithm_label()
        self.create_algorithm_dropdown()

    def create_algorithm_label(self):
        algo_label = tk.Label(self.setup_frame, text="Izvēlies AI algoritmu:")
        algo_label.grid(row=4, column=0, sticky="w", pady=5)

    def create_algorithm_dropdown(self):
        self.algorithm_var = tk.StringVar(value="minimax")
        algo_dropdown = tk.OptionMenu(self.setup_frame, self.algorithm_var, "minimax", "alpha-beta")
        algo_dropdown.grid(row=4, column=1, sticky="ew", pady=5, padx=10)
        algo_dropdown.config(width=15)

    # Row 6
    def create_start_button(self):
        start_button = tk.Button(self.setup_frame, text="Sākt spēli", command=self.start_game, bg="#4CAF50", fg="black", padx=10, pady=5, width=25)
        start_button.grid(row=5, column=0, columnspan=2, pady=(20, 0))

    # Row 7
    def create_autoplay_button(self):
        autoplay_button = tk.Button(self.setup_frame, text="Ļaut datoram spēlēt", bg="#FF9800", fg="black", padx=10, pady=5, width=25)
        # Nonemu command (command=self.autoplay_game) parametru.
        autoplay_button.grid(row=6, column=0, columnspan=2, pady=(10, 0))

    # Row 8
    def create_exit_button(self):
        exit_button = tk.Button(self.setup_frame, text="Beigt spēli", command=self.root.quit, bg="#f44336", fg="black", padx=10, pady=5, width=25)
        exit_button.grid(row=7, column=0, columnspan=2, pady=(20, 0))

    def start_game(self):
        starting_number = self.number_scale.get()
        first_player = self.first_player_var.get()
        self.game_engine = GameState(starting_number, first_player)
        self.setup_frame.destroy()
        # self.create_game_interface()