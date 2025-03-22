from game.game_engine import GameEngine

# Test Case 1
def test_basic_gameplay():
    """Pārbauda pamata spēles mehāniku."""
    print("=== Pārbaudam pamata spēles mehāniku ===")
    
    # Izveido jaunu spēles dzinēju ar sākuma skaitli 10
    engine = GameEngine(10, 'human')
    print(f"Sākotnējais stāvoklis: {engine.state}")
    
    # Cilvēks reizina ar 2 (rezultāts: 20 - pāra)
    engine.make_move(2)
    print(f"Pēc cilvēka (×2): {engine.state}")
    
    # Dators reizina ar 3 (rezultāts: 60 - pāra)
    engine.make_move(3)
    print(f"Pēc datora (×3): {engine.state}")
    
    # Cilvēks reizina ar 3 (rezultāts: 180 - pāra)
    engine.make_move(3)
    print(f"Pēc cilvēka (×3): {engine.state}")
    
    # Dators reizina ar 3 (rezultāts: 540 - pāra)
    engine.make_move(3)
    print(f"Pēc datora (×3): {engine.state}")
    
    # Cilvēks reizina ar 2 (rezultāts: 1080 - pāra, spēle beidzas)
    engine.make_move(2)
    print(f"Pēc cilvēka (×2): {engine.state}")
    
    print(f"Spēle beigusies: {engine.state.is_game_over}")
    print(f"Uzvarētājs: {engine.get_winner()}")

# Test Case 2
def test_odd_result_points():
    """Pārbauda punktu atņemšanu ar nepāra rezultātiem."""
    print("\n=== Pārbauda punktu atņemšanu ar nepāra rezultātiem ===")
    
    # Izveido jaunu spēles dzinēju ar sākuma skaitli 5
    engine = GameEngine(5, 'human')
    print(f"Sākotnējais stāvoklis: {engine.state}")
    
    # Cilvēks reizina ar 3 (rezultāts: 15 - nepāra)
    engine.make_move(3)
    print(f"Pēc cilvēka (×3): {engine.state}")
    
    # Dators reizina ar 3 (rezultāts: 45 - nepāra)
    engine.make_move(3)
    print(f"Pēc datora (×3): {engine.state}")
    
    # Pārbauda, vai punkti ir negatīvi no nepāra rezultātiem
    assert engine.state.human_points == -1
    assert engine.state.computer_points == -1
    print("Punktu pārbaude beigusies!")

# TODO: Izveidot extra test cases un patestēt tās.

if __name__ == "__main__":
    test_basic_gameplay()
    test_odd_result_points()