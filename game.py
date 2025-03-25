class GameState:
    def __init__(self, number, human_score=0, ai_score=0, depth=0, is_human_turn=True, parent=None):
        self.number = number
        self.human_score = human_score
        self.ai_score = ai_score
        self.depth = depth
        self.is_human_turn = is_human_turn
        self.parent = parent

    def __repr__(self):
        return f"Skaitlis={self.number}, Cilvēka punkti={self.human_score}, Datora punkti={self.ai_score}, Dziļums={self.depth}, Vai cilvēka gājiens={self.is_human_turn}"
    
    def generate_next_states(self):
        next_states = []
        for multiplier in [2,3]:
            new_number = self.number * multiplier
            new_human_score, new_ai_score = self.calculate_scores(new_number)
            next_states.append(
                GameState(
                    new_number,
                    human_score=new_human_score,
                    ai_score=new_ai_score,
                    depth=self.depth + 1,
                    is_human_turn=not self.is_human_turn,
                    parent=self
                )
            )
        return next_states
    
    def calculate_scores(self, new_number):
        if new_number % 2 == 0:
            return self.update_scores(1)
        else:
            return self.update_scores(-1)
    
    def update_scores(self, score_change):
        if self.is_human_turn:
            return self.human_score + score_change, self.ai_score
        else:
            return self.human_score, self.ai_score + score_change
    
def print_game_tree(state, max_depth, current_depth=0, prefix=""):
    
    print(f"{prefix}Move {current_depth}: Skaitlis({state.number}), Cilvēks({state.human_score}), Ai({state.ai_score})")
    
    if current_depth >= max_depth:
        return
    
    next_states = state.generate_next_states()

    # AI uzģenerēts
    for i in range(len(next_states)):
        if i == len(next_states) - 1:
            branch_prefix = "└── "  # Last branch
        else:
            branch_prefix = "├── "  # Intermediate branch
        
        print_game_tree(next_states[i], max_depth, current_depth + 1, prefix + branch_prefix)
        
        
"""
Tiek galā ar spēles loģiku, noteikumiem un pāreju starp spēles stāvokļiem (game states).
"""

class GameEngine:
    
    def __init__(self, starting_number, first_player='cilvēks'):
        """
        Inicializē GameEngine.

        Args:
            starting_number (int): skaitlis ar ko sākas spēle. Diapazonā no 5 līdz 15.
            first_player (str): kas iet pirmais ('cilvēks' vai 'dators')
        """
        self.state = GameState(starting_number, first_player)
    
    def make_move(self, multiplier):
        """
        Veikt gājienu spēlē. Spēlētāji veic gājienus pēc kārtas, reizinot pašreizējā brīdī esošu skaitni ar 2 vai 3.
        
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
            int: -1 - cilvēks uzvar, 1 - dators uzvar, 0 - neizšķirts
        """
        if not self.state.is_game_over:
            return None
        
        if self.state.human_points < self.state.computer_points:
            return -1  # cilvēks uzvar
        elif self.state.computer_points < self.state.human_points:
            return 1   # dators uzvar
        else:
            return 0   # neizšķirts
        
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