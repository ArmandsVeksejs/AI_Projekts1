"""
Glabā datus par spēles pašreizējo stāvokli (rezultāti, pašreizējais spēlētājs utt.)

Attributes:
    current_number (int): pašreizējais rezultāts
    human_points (int): cilvēka punktu skaits
    computer_points (int): datora punktu skaits
    current_player (str): pašreizējais spēlētājs (dators vai cilvēks)
    is_game_over (bool): vai spēles ir beigusies (ir sasniegts rezultāts = 1000)
"""

class GameState:
    
    def __init__(self, starting_number, first_player='cilvēks'):
        """
        Inicializē GameState

        Args:
            starting_number (int): skaitlis (rezultāts), ar ko sākt spēli
            first_player (str): kas iet pirmais (dators vai cilvēks), uzd nosacījumos šis ir cilvēks, tpc šeit tas norādīts kā default
        """
        self.current_number = starting_number
        self.human_points = 0
        self.computer_points = 0
        self.current_player = first_player
        self.is_game_over = False
    
    def is_terminal(self):
        """
        Pārbauda vai spēle beigusies. Spēle beidzas, kā tikko ir iegūts skaitlis, kas ir lielāks vai vienāds ar 1000.

        Returns:
            bool: True ja sasniegusi, False ja ne
        """
        return self.current_number >= 1000
    
    def get_possible_moves(self):
        return [2, 3]
    
    def copy(self):
        """
        Izveido spēles stāvokļa kopiju.
        
        Returns:
            GameState: A new identical game state
        """
        new_state = GameState(self.current_number, self.current_player)
        new_state.human_points = self.human_points
        new_state.computer_points = self.computer_points
        new_state.is_game_over = self.is_game_over
        return new_state
    
    def __str__(self):
        """
        Metode `__str__` nosaka, kā objektu izvadīt teksta formā.

        Returns:
            String: Spēles stāvoklis teksta formā.
        """
        return (f"Number: {self.current_number}, "
                f"Human: {self.human_points} points, "
                f"Computer: {self.computer_points} points, "
                f"Current player: {self.current_player}")