class GameEngine:
    def __init__(self, number, human_score=0, ai_score=0, depth=0, is_human_turn=True):
        self.number = int(number)
        self.human_score = int(human_score)
        self.ai_score = int(ai_score)
        self.depth = int(depth)
        self.is_human_turn = is_human_turn
        self.is_game_over = self.number >= 1000
        self.human_wins = 0
        self.ai_wins = 0

    
    # Atgriež spēlētāja nosaukumu
    def current_player(self):
        return "cilvēks" if self.is_human_turn else "dators"

    
    # Pārbauda, vai spēle ir beigusies
    def is_terminal(self):
        return self.number >= 1000

    
    # Izveido kopiju no esošā spēles stāvokļa
    def copy(self):
        return GameEngine(
            self.number,
            self.human_score,
            self.ai_score,
            self.depth,
            self.is_human_turn
        )

    
    # Atgriež spēles stāvokļa aprakstu
    def __repr__(self):
        return (f"Number: {self.number}, "
                f"Human: {self.human_score} points, "
                f"AI: {self.ai_score} points, "
                f"Player: {self.current_player()}, "
                f"Depth: {self.depth}")

    
    # Aprēķina punktus jaunajā stāvoklī
    def calculate_scores(self, new_number):
        return self.update_scores(1 if new_number % 2 == 0 else -1)

    
    # Atjaunina spēlētāju punktus
    def update_scores(self, score_change):
        if self.is_human_turn:
            return self.human_score + score_change, self.ai_score
        else:
            return self.human_score, self.ai_score + score_change

    
    # Aprēķina punktus, pamatojoties uz spēles stāvokli
    def calculate_points(self, state):
        if state.number % 2 == 0:               
            if state.is_human_turn:
                state.human_score += 1
            else:
                state.ai_score += 1
        else:                                           
            if state.is_human_turn:
                state.human_score -= 1
            else:
                state.ai_score -= 1

    
    # Veic spēles gājienu
    def make_move(self, multiplier):
        if self.is_game_over:
            return False

        self.number *= multiplier

        # Aprēķina punktus pašreizējam spēlētājam
        if self.number % 2 == 0:
            if self.is_human_turn:
                self.human_score += 1
            else:
                self.ai_score += 1
        else:
            if self.is_human_turn:
                self.human_score -= 1
            else:
                self.ai_score -= 1

        self.is_human_turn = not self.is_human_turn
        self.is_game_over = self.is_terminal()
        return True

    
    # AI veic gājienu, pamatojoties uz labāko rezultātu
    def ai_move(self):
        if self.is_game_over:
            return

        best_multiplier = None
        best_score = float('-inf')

        for multiplier in [2, 3]:
            # Simulē kopētu stāvokli
            simulated = self.copy()
            simulated.make_move(multiplier)

            # AI vērtē savu punktu pārsvaru
            score_diff = simulated.ai_score - simulated.human_score

            if score_diff > best_score:
                best_score = score_diff
                best_multiplier = multiplier

        if best_multiplier:
            self.make_move(best_multiplier)

    
    # Atgriež uzvarētāja tekstu
    def get_winner_text(self):
        if self.human_score < self.ai_score:
            return "Tu uzvarēji!"
        elif self.ai_score < self.human_score:
            return "Dators uzvarēja!"
        else:
            return "Neizšķirts!"

    
    # Ģenerē nākamos spēles stāvokļus
    def generate_next_states(self):
        next_states = []
        for multiplier in [2, 3]:
            new_number = self.number * multiplier
            new_human_score, new_ai_score = self.calculate_scores(new_number)
            next_states.append(GameEngine(
                new_number,
                new_human_score,
                new_ai_score,
                depth=self.depth + 1,
                is_human_turn=not self.is_human_turn,
                parent=self
            ))
        return next_states