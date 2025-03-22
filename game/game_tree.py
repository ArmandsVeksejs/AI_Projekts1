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
        Virsotnes inicializēšana.
        
        Args:
            state (GameState): spēles stāvoklis
            move (int, optional): loks (spēles gājiens)
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
        """Virsotnes teksta reprezentācija."""
        move_str = f" (gājiens: ×{self.move})" if self.move else ""
        return f"Node{move_str}: {self.state}"

class GameTree:
    """
    Spēles koks dažādu spēles stāvokļu izpētei.
    """
    
    def __init__(self, initial_state):
        """
        Jauna spēles koka izveide.
        
        Args:
            initial_state (GameState): spēles sākuma stāvoklis
        """
        self.root = Node(initial_state)
        # Virsotņu skaits priekš statistikas
        self.nodes_count = 1
    
    def expand_node(self, node, depth=1):
        """
        Expand a node to a certain depth.
        
        Args:
            node (Node): The node to expand
            depth (int): How many levels to expand
            
        Returns:
            Node: The expanded node
        """
        # Base case: if depth is 0 or node is terminal, stop expansion
        if depth <= 0 or node.state.is_terminal():
            return node
        
        # Get possible moves from this state
        possible_moves = [2, 3]  # Can multiply by 2 or 3
        
        # Create a temporary game engine to apply moves
        engine = GameEngine(node.state.current_number, node.state.current_player)
        engine.state = node.state.copy()  # Use a copy of the node's state
        
        # For each possible move
        for move in possible_moves:
            # Create a copy of the current state
            temp_engine = GameEngine(engine.state.current_number, engine.state.current_player)
            temp_engine.state = engine.state.copy()
            
            # Apply the move
            if temp_engine.make_move(move):
                # Create a new node for the resulting state
                child_node = Node(temp_engine.state.copy(), move=move, parent=node)
                # Add the child to the current node
                node.add_child(child_node)
                # Increment node count
                self.nodes_count += 1
                # Recursively expand the child node
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
        
        # Izmantot rekursiju, lai izprintētu visus pēctečus palielinot dziļumu par 1 katru reizi, kas funkcija tiek izpildīta
        for child in node.children:
            self.print_tree(child, depth + 1)
    
    def get_nodes_count(self):
        """
        Iegūt virsotņu skaitu
        
        Returns:
            int: Kopējais virsotņu skaits
        """
        return self.nodes_count