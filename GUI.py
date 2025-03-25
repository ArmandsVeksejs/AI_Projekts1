import tkinter as tk
from tkinter import messagebox
from game import GameEngine

class GUI:
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
        self.create_algorithm_selection()
        self.create_start_button()
        self.create_autoplay_button()
        self.create_exit_button()
        
    def create_exit_button(self):
        
        exit_button = tk.Button(self.setup_frame, text="Beigt spēli", command=self.root.quit, bg="#f44336", fg="black", padx=10, pady=5, width=25)
        exit_button.grid(row=7, column=0, columnspan=2, pady=(20, 0))
    
    def create_description(self):
        
        """
        Spēles apraksts.
        """
        title_label = tk.Label(self.setup_frame, text="Skaitļu reizināšanas spēle", font=("Arial", 18, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        description_label = tk.Label(
            self.setup_frame, 
            text="Spēles sākumā ir dots cilvēka-spēlētāja izvēlētais skaitlis. Abiem spēlētājiem ir 0 punktu. "
                "Spēlētāji veic gājienus pēc kārtas, reizinot pašreizējā brīdī esošu skaitni ar 2 vai 3. "
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
            
    def create_algorithm_selection(self):
        
        """
        Ļauj lietotājam izvēlēties, kuru algoritmu dators izmantos.
        """
        algo_label = tk.Label(self.setup_frame, text="Izvēlies AI algoritmu:")
        algo_label.grid(row=4, column=0, sticky="w", pady=5)

        self.algorithm_var = tk.StringVar(value="vienkāršs")
        algo_options = ["vienkāršs", "minimax", "alpha-beta"]
        algo_dropdown = tk.OptionMenu(self.setup_frame, self.algorithm_var, *algo_options)
        algo_dropdown.grid(row=4, column=1, sticky="ew", pady=5, padx=10)
        algo_dropdown.config(width=15)

    def create_start_button(self):
        
        start_button = tk.Button(self.setup_frame, text="Sākt spēli", command=self.start_game, bg="#4CAF50", fg="black", padx=10, pady=5, width=25)
        start_button.grid(row=5, column=0, columnspan=2, pady=(20, 0))
    
    def create_autoplay_button(self):
        
        autoplay_button = tk.Button(self.setup_frame, text="Ļaut datoram spēlēt", command=self.autoplay_game, bg="#FF9800", fg="black", padx=10, pady=5, width=25)
        autoplay_button.grid(row=6, column=0, columnspan=2, pady=(10, 0))
        
    def autoplay_game(self):
        
        selected_algorithm = self.algorithm_var.get()
        starting_number = self.number_scale.get()
        first_player = "dators"
        self.game_engine = GameEngine(starting_number, first_player)
        self.setup_frame.destroy()

        self.autoplay_frame = tk.Frame(self.root, padx=20, pady=20)
        self.autoplay_frame.pack(expand=True, fill="both")

        steps = []
        while not self.game_engine.state.is_game_over:
            current = self.game_engine.state.current_number

            # Gudrāka izvēle starp 2 un 3
            best_move = None
            best_score = float('-inf')

            for move_option in [2, 3]:
                simulated_state = self.game_engine.state.copy()
                simulated_state.current_number *= move_option

                if simulated_state.current_number % 2 == 0:
                    simulated_state.computer_points += 1
                else:
                    simulated_state.computer_points -= 1

                score = -simulated_state.computer_points

                if score > best_score:
                    best_score = score
                    best_move = move_option

            move = best_move
            self.game_engine.make_move(move)
            steps.append(f"{current} x{move} = {self.game_engine.state.current_number}")

        text_widget = tk.Text(self.autoplay_frame, wrap="word")
        text_widget.pack(expand=True, fill="both", padx=10, pady=10)

        for step in steps:
            text_widget.insert("end", step + "\n")
        text_widget.config(state="disabled")

        algo_label = tk.Label(self.autoplay_frame, text=f"Algoritms: {selected_algorithm}", font=("Arial", 20), fg="white")
        algo_label.pack(pady=(10, 0))

        self.play_again_button = tk.Button(self.autoplay_frame, text="Atpakaļ uz izvēlni", command=self.return_to_menu_from_autoplay, bg="#f44336", fg="black", padx=10, pady=5)
        self.play_again_button.pack(pady=10)

    def return_to_menu_from_autoplay(self):
        if hasattr(self, 'autoplay_frame'):
            self.autoplay_frame.destroy()
        if hasattr(self, 'play_again_button'):
            self.play_again_button.destroy()
        self.create_setup_panel()
        
    def create_game_interface(self):
        
        self.game_frame = tk.Frame(self.root, padx=20, pady=20)
        self.game_frame.pack(expand=True)

        # Pašreizējais skaitlis
        self.number_label = tk.Label(self.game_frame, text=f"Skaitlis: {self.game_engine.state.current_number}", font=("Arial", 24))
        self.number_label.pack(pady=10)

        # Punkti
        self.points_label = tk.Label(self.game_frame, text=self.get_points_text(), font=("Arial", 14))
        self.points_label.pack(pady=5)

        # Gājiena pogas
        self.move_buttons = tk.Frame(self.game_frame)
        self.move_buttons.pack(pady=10)

        # Reizināt ar 2 poga
        btn2 = tk.Button(self.move_buttons, text="x2", command=lambda: self.player_move(2),
                         font=("Arial", 16), width=8)
        btn2.pack(side="left", padx=15, pady=10)
        btn2.bind("<Enter>", lambda e: btn2.config(bg="#c6f5d7"))
        btn2.bind("<Leave>", lambda e: btn2.config(bg="SystemButtonFace"))

        # Reizināt ar 3 poga
        btn3 = tk.Button(self.move_buttons, text="x3", command=lambda: self.player_move(3),
                         font=("Arial", 16), width=8)
        btn3.pack(side="left", padx=15, pady=10)
        btn3.bind("<Enter>", lambda e: btn3.config(bg="#ffe0b3"))
        btn3.bind("<Leave>", lambda e: btn3.config(bg="SystemButtonFace"))

        # Ja dators sāk
        if self.game_engine.state.current_player == "dators":
            self.root.after(500, self.ai_move)
            
    def get_points_text(self):
        
        return f"Cilvēks: {self.game_engine.state.human_points} | Dators: {self.game_engine.state.computer_points}"
    
    
    def player_move(self, multiplier):
        
        self.game_engine.make_move(multiplier)

        if self.game_engine.state.is_game_over:
            self.update_display()
            self.show_winner()
        else:
            self.update_display()

        if self.game_engine.state.current_player == "dators":
            self.root.after(500, self.ai_move)

    def ai_move(self):
        best_move = None
        best_score = float('-inf')

        for move in [2, 3]:
            # Simulate the move
            simulated_state = self.game_engine.state.copy()
            simulated_state.current_number *= move

            # Simulate point update
            if simulated_state.current_number % 2 == 0:
                if simulated_state.current_player == "dators":
                    simulated_state.computer_points += 1
                else:
                    simulated_state.human_points += 1
            else:
                if simulated_state.current_player == "dators":
                    simulated_state.computer_points -= 1
                else:
                    simulated_state.human_points -= 1

            # Evaluate score (lower is better for computer)
            score = simulated_state.human_points - simulated_state.computer_points

            if score > best_score:
                best_score = score
                best_move = move

        self.game_engine.make_move(best_move)

        if self.game_engine.state.is_game_over:
            self.update_display()
            self.show_winner()
        else:
            self.update_display()

    def update_display(self):
        self.number_label.config(text=f"Skaitlis: {self.game_engine.state.current_number}")
        self.points_label.config(text=self.get_points_text())

    def show_winner(self):
        
        """
        Parada uzvaretaju pec speles izspelesanas , ka ari pievienotas pogas spelet velreiz un beigt speli
        """
        
        if hasattr(self, 'winner_shown') and self.winner_shown:
            return
        self.winner_shown = True

        state = self.game_engine.state
        
        if state.human_points < state.computer_points:
            msg = "Tu uzvareji!"
        elif state.human_points > state.computer_points:
            msg = "Dators uzvareja!"
        else:
            msg = "Neizskirts!"
            
       
        self.winner_label = tk.Label(self.game_frame, text=msg, font=("Arial", 18), fg="gold", bg="#333333")
        self.winner_label.pack(pady = 20)
        self.play_again_button = tk.Button(self.root, text="Spēlēt vēlreiz", command=self.restart_game, bg="#2196F3", fg="black", padx=10, pady=5, width=25)
        self.play_again_button.pack(pady = 10)
        self.end_game_button = tk.Button(self.root, text="Beigt spēli", command=self.root.quit, bg="#f44336", fg="black", padx=10, pady=5, width=25)
        self.end_game_button.pack(pady = 10)

        for widget in self.move_buttons.winfo_children():
            widget.config(state = 'disabled')

    
    def restart_game(self):
        
        self.end_game_button.destroy()
        self.winner_label.destroy()
        self.play_again_button.destroy()
        self.game_frame.destroy()
        self.create_setup_panel()
        self.winner_shown = False
    
    def start_game(self):
        
        """
        Palaiž spēli. No sākuma tiek izveidots logs, kurā cilvēks norāda spēles parametrus (skaitli, kas sāk, kurš algoritms)
        """
        starting_number = self.number_scale.get()
        first_player = self.first_player_var.get()
        self.game_engine = GameEngine(starting_number, first_player)
        self.setup_frame.destroy()
        self.create_game_interface()