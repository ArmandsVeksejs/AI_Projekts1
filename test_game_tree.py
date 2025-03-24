from game.game_state import GameState
from game.game_tree import GameTree

def test_game_tree():
    """Šī funkcija vizualizē koku"""
    # Sākuma stāvokļa norāde (var pievienot vēl vienu parametru "dators", lai spēli sāktu dators)
    initial_state = GameState(100)
    
    # Spēles koka izveide
    tree = GameTree(initial_state)
    
    # Paplašināt koku līdz noteiktam dziļumam
    exploration_depth = 3
    print(f"Paplašinam koku līdz dziļumam {exploration_depth}...")
    tree.expand_node(tree.root, exploration_depth)
    
    print(f"Kopējais mezglu skaits: {tree.get_nodes_count()}")

    print("\nKoka struktūra:")
    tree.print_tree()

if __name__ == "__main__":
    test_game_tree()