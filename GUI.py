import tkinter as tk
from tkinter import messagebox
from game_tree import GameState
from algoritmi import minimax, alpha_beta

class gui:
    def __init__(self, root):
        self.root = root
        self.root.title("Spēle")
        self.root.geometry("800x600")
        self.human_wins = 0
        self.ai_wins = 0
        self.draws = 0
        self.result_recorded = False
        self.create_setup_panel()

    # Sākuma logs
    def create_setup_panel(self):
        self.setup_frame = tk.Frame(self.root, padx=20, pady=20)
        self.setup_frame.pack(expand=True)
        self.win_counter_label = tk.Label(
            self.setup_frame,
            text=f"Uzvaras: Tu: {self.human_wins}   Dators: {self.ai_wins}   Neizšķirti: {self.draws}",
            font=("Arial", 12),
            relief="groove", bd=2, padx=10, pady=5
        )
        self.win_counter_label.grid(row=6, column=0, columnspan=2, pady=(10, 10))
        self.create_title()
        self.create_description()
        self.create_number_selection()
        self.create_player_selection()
        self.create_algorithm_selection()
        self.create_start_button()
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
            height=12,
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
        self.number_scale = tk.Scale(self.setup_frame, from_=5, to=15, orient=tk.HORIZONTAL, length=200)
        self.number_scale.grid(row=2, column=1, pady=5, padx=10, sticky="ew")

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
        start_button.grid(row=5, column=0, pady=(20, 0), padx=(0, 5), sticky="e")

    # Row 7
    def create_exit_button(self):
        exit_button = tk.Button(self.setup_frame, text="Beigt spēli", command=self.root.quit, bg="#f44336", fg="black", padx=10, pady=5, width=25)
        exit_button.grid(row=5, column=1, pady=(20, 0), padx=(5, 0), sticky="w")

    # Spēles sākšana
    def start_game(self):
        starting_number = self.number_scale.get()
        first_player = self.first_player_var.get()
        self.starting_number = starting_number
        self.first_player = first_player
        self.algorithm = self.algorithm_var.get()
        self.state = GameState(starting_number, 0, 0, 0, is_human_turn=(first_player == "cilvēks"))
        self.setup_frame.destroy()
        self.create_game_interface()
        if self.state.is_human_turn is False:
            self.root.after(500, self.loop_ai_turn)

    def restart_game(self):
        self.game_frame.destroy()
        self.result_recorded = False
        self.state = GameState(self.starting_number, 0, 0, 0, is_human_turn=(self.first_player == "cilvēks"))
        self.create_game_interface()
        if self.state.is_human_turn is False:
            self.root.after(500, self.loop_ai_turn)

    
    def back_to_menu(self):
        self.game_frame.destroy()
        self.result_recorded = False
        self.create_setup_panel()

    
    # Spēles logs
    def create_game_interface(self):
        self.game_frame = tk.Frame(self.root, padx=20, pady=20)
        self.game_frame.pack(expand=True)

        # Pašreizējais skaitlis
        self.number_label = tk.Label(self.game_frame, text=f"Skaitlis: {self.state.number}", font=("Arial", 24))
        self.number_label.pack(pady=10)

        # Punkti
        self.points_label = tk.Label(self.game_frame, text=self.get_points_text(), font=("Arial", 14))
        self.points_label.pack(pady=5)

        # Gājiena pogas
        self.move_buttons = tk.Frame(self.game_frame)
        self.move_buttons.pack(pady=10)

        # Reizināt ar 2 poga
        btn2 = tk.Button(self.move_buttons, text="x2", command=lambda: self.human_then_ai_move(2), font=("Arial", 16), width=8)
        btn2.pack(side="left", padx=15, pady=10)
        btn2.bind("<Enter>", lambda e: btn2.config(bg="#c6f5d7"))
        btn2.bind("<Leave>", lambda e: btn2.config(bg="SystemButtonFace"))

        # Reizināt ar 3 poga
        btn3 = tk.Button(self.move_buttons, text="x3", command=lambda: self.human_then_ai_move(3), font=("Arial", 16), width=8)
        btn3.pack(side="left", padx=15, pady=10)
        btn3.bind("<Enter>", lambda e: btn3.config(bg="#ffe0b3"))
        btn3.bind("<Leave>", lambda e: btn3.config(bg="SystemButtonFace"))

    
    def get_points_text(self):
        return f"Cilvēks: {self.state.human_score} punkti     Dators: {self.state.ai_score} punkti"

    
    def update_ui(self):
        if not hasattr(self, "number_label") or not hasattr(self, "points_label"):
            return
        
        if self.state.number >= 1000 and not self.result_recorded:
            if self.state.human_score < self.state.ai_score:
                self.human_wins += 1
            elif self.state.ai_score < self.state.human_score:
                self.ai_wins += 1
            else:
                self.draws += 1
            self.result_recorded = True

        self.number_label.config(text=f"Skaitlis: {self.state.number}")
        self.points_label.config(text=self.get_points_text())
        
        if self.state.number >= 1000:
            self.points_label.pack_forget()

        if self.state.number >= 1000:
            self.move_buttons.pack_forget()

            self.result_label = tk.Label(self.game_frame, text=self.get_winner_text(), font=("Arial", 22, "bold"), fg="white", padx=10, pady=5)
            self.result_label.pack(pady=10)

            self.final_points_label = tk.Label(self.game_frame, text=self.get_points_text(), font=("Arial", 14), relief="groove", bd=2, padx=10, pady=5)
            self.final_points_label.pack(pady=5)

            self.create_end_buttons()

        if hasattr(self, "win_counter_label") and self.win_counter_label.winfo_exists():
            self.win_counter_label.config(
                text=f"Uzvaras: Tu: {self.human_wins}   Dators: {self.ai_wins}   Neizšķirti: {self.draws}"
            )

    
    # Spēles beigu darbības
    def create_end_buttons(self):
        self.end_buttons_frame = tk.Frame(self.game_frame)
        self.end_buttons_frame.pack(pady=10)

        restart_btn = tk.Button(self.end_buttons_frame, text="Spēlēt vēlreiz", command=self.restart_game, bg="#4CAF50", fg="black", padx=10, pady=5, width=20)
        restart_btn.pack(side="left", padx=10)

        menu_btn = tk.Button(self.end_buttons_frame, text="Atgriezties uz izvēlni", command=self.back_to_menu, bg="#2196F3", fg="black", padx=10, pady=5, width=20)
        menu_btn.pack(side="left", padx=10)

    
    # Spēlētāja un AI gājieni
    def human_then_ai_move(self, multiplier):
        self.state = self.state.generate_next_state(multiplier)
        self.update_ui()

        if not self.state.number >= 1000 and not self.state.is_human_turn:
            self.root.after(500, self.loop_ai_turn)

    def loop_ai_turn(self):
        if not self.state.is_human_turn and self.state.number < 1000:
            best_score = float('-inf')
            best_state = None

            if self.algorithm == "minimax":
                score, best_state = minimax(5, self.state, True)
            else:
                score = alpha_beta(5, self.state, True, float('-inf'), float('inf'))
                # alpha_beta neatgriež stāvokli, tāpēc atrod to atkārtoti
                for child in self.state.generate_next_states():
                    child_score = alpha_beta(4, child, False, float('-inf'), float('inf'))
                    if child_score == score:
                        best_state = child
                        break
            if best_state:
                self.state = best_state
            
            self.update_ui()
            if not self.state.is_human_turn and self.state.number < 1000:
                self.root.after(500, self.loop_ai_turn)

    def get_winner_text(self):
        if self.state.human_score < self.state.ai_score:
            return "Tu uzvarēji!"
        elif self.state.ai_score < self.state.human_score:
            return "Dators uzvarēja!"
        else:
            return "Neizšķirts!"