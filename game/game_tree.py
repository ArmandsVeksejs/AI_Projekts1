from game.game_engine import GameEngine

class Node:
    """
    Virsotne spēles kokā.
    
    Attributes:
        state (GameState): pašreizējais stāvoklis šajā virsotnē
        children (list): pēcteči
        move (int): loks (spēles kokā)
        parent (Node): priekštecis
    """
    
    def __init__(self, state, move=None, parent=None):
        """
        Inicializẽ virsotni.
        
        Args:
            state (GameState): spēles pašreizējais stāvoklis
            move (int, optional): kāds gājiens tika veikts
            parent (Node, optional): priekštecis
        """
        self.state = state
        self.children = []
        self.move = move
        self.parent = parent
    
    def add_child(self, child_node):
        """
        Pievienot pēcteci virsotnei.
        
        Args:
            child_node (Node): pēctecis, kas tiek pievienots
        """
        self.children.append(child_node)
        
    def __str__(self):
        """
        Metode `__str__` nosaka, kā objektu izvadīt teksta formā.

        Returns:
            String: Virsotne teksta formā
        """
        move_str = f" (gājiens: ×{self.move})" if self.move else ""
        return f"Node{move_str}: {self.state}"

class GameTree:
    def __init__(self, initial_state):
        """
        Inicializē spēles koku.
        
        Args:
            initial_state (GameState): spēles sākuma stāvoklis
        """
        self.root = Node(initial_state)
        self.nodes_count = 1
    
    def expand_node(self, node, depth=1):
        """
        Ğenerē spēles koku līdz noteiktam dziļumam.
        
        Args:
            node (Node): virsotne, ko izpētīt
            depth (int): dziļums
            
        Returns:
            Node: The expanded node
        """
        if depth <= 0 or node.state.is_terminal():
            return node
        
        possible_moves = [2, 3]
        engine = GameEngine(node.state.current_number, node.state.current_player)
        
        for move in possible_moves:
            engine.state = node.state.copy()
            if engine.make_move(move):
                child_node = Node(engine.state.copy(), move=move, parent=node)
                node.add_child(child_node)
                self.nodes_count += 1
                self.expand_node(child_node, depth - 1)
        
        return node
    
    def print_tree(self, node=None, depth=0, prefix=""):
        """
        Spēles koka izvade vizuālā formātā (2D teksts).
        
        Args:
            node (Node, optional): Virsotne, no kuras sākt izvadīt koku
            depth (int): Pašreizējais dziļums
            prefix (str): Prefikss, ko izmantot atkāpēm
        """
        
        if node is None:
            node = self.root
        
        # Ar katru līmeni pievienot tab simbolu
        indent = "\t" * depth
        
        # Virsotnes stāvokļa informācija izvade
        current_number = f"Skaitlis: {node.state.current_number}"
        player_points = f"Cilvēks: {node.state.human_points} | Dators: {node.state.computer_points}"
        
        # Izvadīt kustību (x2 vai x3)
        move_info = f"[×{node.move}]" if node.move else "[Sākums]"
        
        # Izvadīt virsotni
        print(f"{indent}{move_info} {current_number} | {player_points}")
        
        # Izmantot rekursiju, lai izprintētu visus pēctečus palielinot dziļumu par 1 katru reizi, kad funkcija tiek izpildīta
        for child in node.children:
            self.print_tree(child, depth + 1)
    
    def get_nodes_count(self):
        """
        Iegūt virsotņu skaitu
        
        Returns:
            int: Kopējais virsotņu skaits
        """
        return self.nodes_count