def alpha_beta():
    pass

def minimax():
    pass

def heuristic(self):
    # Mērķis - mazāks punktu skaits nekā pretiniekam
    # Viss, kas tiecas pretī šim mērķim dod pozitīvu vērtību
    # Pretinieks - spēlētājs, kurš nesāka spēli
    score_difference = self.ai_score - self.human_score
    # Izveido vērtību no 0 līdz 1, kas norāda, cik tuvu mēs esam spēles beigu stāvoklim (1000).
    # Spēle tiek sadalīta fāzēs, pamatojoties uz pašreizējo skaitli.
    proximity_to_end = min(1.0, (self.number / 500)**2)

    # Izvērtē, kuri skaitļi (pāra/ nepāra) tiek iegūti pēc nākamā gājiena:
    def future_parity_impact():
        next_numbers = [self.number * 2, self.number * 3]
        even_count = sum(1 for num in next_numbers if num % 2 == 0)
        odd_count = sum(1 for num in next_numbers if num % 2 == 1)

        if odd_count == 2:
            return 1.0
        elif even_count == 2:
            return -1.0
        return 0
    
    # Izvērtē spēli nākotnei. Ļauj AI iepriekš saprast, kā tuvākajā nākotnē mainīsies punktu bilance, un pieņemt jēgpilnākus lēmumus.
    def future_score_change():
        next_states = self.generate_next_states()
        if not next_states:
            return 0
        return sum((s.ai_score - s.human_score) for s in next_states) / len(next_states)
    
    # AI tagad novērš iespējamos ienaidnieka uzbrukumus, padarot to reālistiskāku un grūtāk uzveicamu.
    def opponent_future_impact():
        next_states = self.generate_next_states()
        if not next_states:
            return 0
        opponent_advantages = [-s.evaluate() for s in next_states]
        return max(opponent_advantages)
    
    # Funkcija move_freedom() padara AI stratēģiskāku un mazāk paredzamu. Tagad atstājiet sev vairāk gājienu iespēju.
    def move_freedom():
        next_states = self.generate_next_states()
        if not next_states:
            return 0
        return (len(set(s.number for s in next_states)) / len(next_states)) * (1 - proximity_to_end)
    
    # Funkcija unavoidable_penalty() soda situācijas, kad AI izvēlējās gājienus, pēc kuriem visi turpmākie skaitļi kļūst pāra skaitļi.
    def unavoidalbe_penalty():
        next_numbers = [self.number * 2, self.number * 3]
        if all(num % 2 == 0 for num in next_numbers):
            return -0.8
        
        parity_advantage = 0.7 if self.number % 2 == 1 and self.is_human_turn else -0.7
        parity_advantage += future_parity_impact()
        future_options = future_score_change()

        immediate_value = score_difference * (0.5 + 0.5 * proximity_to_end)
        strategic_value = (parity_advantage + future_options - opponent_future_impact()) * (1 - 0.5 * proximity_to_end)
        strategic_value += move_freedom() * 0.5
        strategic_value += unavoidalbe_penalty() or 0

        return immediate_value + strategic_value