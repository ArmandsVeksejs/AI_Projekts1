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