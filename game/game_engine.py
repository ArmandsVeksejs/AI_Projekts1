"""
Šī klase tiek galā ar spēles noteikumiem
"""
from game.game_state import GameState

class GameEngine:
    
    def __init__(self, starting_number, first_player='cilvēks'):
        """
        Sākt jaunu spēli
        
        Args:
            starting_number (int): skaitlis ar ko sākas spēle
            first_player (str): kas iet pirmais ('cilvēks' vai 'dators')
        """
        self.state = GameState(starting_number, first_player)
    
    def make_move(self, multiplier):
        """
        Veikt gājienu spālē
        
        Args:
            multiplier (int): 2 vai 3 šis ir skaitlis, ar kuru reizinām atbilstoši spēles nosacījumiem
            
        Returns:
            bool: True ja gājiens veiksmīgs, False ja ne
        """
        if self.state.is_game_over:
            return False
        
        # izveidot jaunu stāvokli
        new_state = self.state.copy()
        new_state.current_number *= multiplier
        self.calculate_points(new_state)

        # Mainīt spēlētāju
        new_state.current_player = 'dators' if new_state.current_player == 'cilvēks' else 'cilvēks'
        
        new_state.is_game_over = new_state.is_terminal()
        
        self.state = new_state
        return True
    
    def calculate_points(self, state):
        """
        Aprēķināt un atjaunināt punktu skaitu pēc gājiena
        
        Args:
            state (GameState): spēles stāvoklis, ko mainīsim
            old_number (int): skaitlis pirms gājiena
        """
        if state.current_number % 2 == 0:  # Pāra rezultāts
            if state.current_player == 'cilvēks':
                state.human_points += 1
            else:
                state.computer_points += 1
        else:  # Nepāra rezultāts
            if state.current_player == 'cilvēks':
                state.human_points -= 1
            else:
                state.computer_points -= 1
    
    def check_game_over(self):
        """
        Pārbaudīt vai spēle is beigusies
        
        Returns:
            bool: True - ir beigusies, False - nav beigusies
        """
        return self.state.is_terminal()
    
    def get_winner(self):
        """
        Noteikt spēles uzvarētāju
        
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
            return 'neizšķirts'