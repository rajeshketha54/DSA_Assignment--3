# Print the nodes at odd levels of a tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    def print_nodes_at_odd_levels(self):
        self._print_nodes_at_odd_levels_recursive(self.root, 1)
    def _print_nodes_at_odd_levels_recursive(self, node, level):
        if node is None:
            return
        if level % 2 == 1:
            print(node.data)
        self._print_nodes_at_odd_levels_recursive(node.left, level + 1)
        self._print_nodes_at_odd_levels_recursive(node.right, level + 1)
        
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print("Nodes at odd levels:")
tree.print_nodes_at_odd_levels()
