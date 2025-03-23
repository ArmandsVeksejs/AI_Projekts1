"""
Tiek galā ar spēles loģiku, noteikumiem un pāreju starp spēles stāvokļiem (game states).
"""
from game.game_state import GameState

class GameEngine:
    
    def __init__(self, starting_number, first_player='cilvēks'):
        """
        Inicializē GameEngine.

        Args:
            starting_number (int): skaitlis ar ko sākas spēle. Diapazonā no 5 līdz 15.
            first_player (str): kas iet pirmais ('cilvēks' vai 'dators')
        """
        # TODO: Uzlikt limitu skaitļa diapazonam.
        self.state = GameState(starting_number, first_player)
    
    def make_move(self, multiplier):
        """
        Veikt gājienu spēlē. Spēlētāji veic gājienus pēc kārtas, reizinot pašreizējā brīdī esošu skaitli ar 2 vai 3.
        
        Args:
            multiplier (int): 2 vai 3 šis ir skaitlis, ar kuru reizinām atbilstoši spēles nosacījumiem
            
        Returns:
            bool: True ja gājiens veiksmīgs, False ja ne
        """
        if self.state.is_game_over:
            return False
        
        new_state = self.state.copy()
        new_state.current_number *= multiplier
        self.calculate_points(new_state)
        new_state.current_player = 'dators' if new_state.current_player == 'cilvēks' else 'cilvēks'
        new_state.is_game_over = new_state.is_terminal()
        self.state = new_state

        return True
    
    def calculate_points(self, state):
        """
        Aprēķina punktu skaitu spēlētājiem. Ja reizināšanas rezultātā tiek iegūts pāra skaitlis, tad spēlētāja punktu skaitam tiek pieskaitīts 1 punkts, bet ja nepāra skaitlis, tad 1 punkts tiek atņemts
        
        Args:
            state (GameState): spēles stāvoklis, ko mainīsim
        """
        if state.current_number % 2 == 0:               # Pāra skaitlis
            if state.current_player == 'cilvēks':
                state.human_points += 1
            else:
                state.computer_points += 1
        else:                                           # Nepāra skaitlis
            if state.current_player == 'cilvēks':
                state.human_points -= 1
            else:
                state.computer_points -= 1
    
    def check_game_over(self):
        """
        Pārbauda vai spēle is beigusies.
        
        Returns:
            bool: True - ir beigusies, False - nav beigusies
        """
        return self.state.is_terminal()
    
    def get_winner(self):
        """
        Nosaka spēles uzvarētāju. Spēlētājs ar mazāko punktu skaitu uzvar spēli. Ja punktu skaits ir vienāds, tad rezultāts ir neizšķirts.
        
        Returns:
            str: 'cilvēks', 'dators', vai 'neizšķirts'
        """
        if not self.state.is_terminal():
            return None
        
        if self.state.human_points < self.state.computer_points:
            return 'cilvēks'  # Cilvēks uzvar ar mazāk punktiem
        elif self.state.computer_points < self.state.human_points:
            return 'dators'  # Dators uzvar ar mazāk punktiem
        else:
            return 'neizšķirts' # Punktu skaits ir vienāds