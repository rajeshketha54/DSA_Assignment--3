# Function to print all the leaves in a given binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def print_leaves(self):
        self._print_leaves_recursive(self.root)

    def _print_leaves_recursive(self, node):
        if node is None:
            return

        if node.left is None and node.right is None:
            print(node.data, end=" ")

        self._print_leaves_recursive(node.left)
        self._print_leaves_recursive(node.right)
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("Leaves of the binary tree:",end=" ")
tree.print_leaves()

