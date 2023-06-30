# Find sum of all nodes of the given perfect binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def calculate_sum(self):
        height = self._calculate_height(self.root)
        total_nodes = (2 ** height) - 1
        return self._calculate_sum_recursive(self.root, total_nodes)

    def _calculate_sum_recursive(self, node, total_nodes):
        if node is None:
            return 0
        return (node.data * total_nodes) + self._calculate_sum_recursive(node.left, total_nodes // 2) + self._calculate_sum_recursive(node.right, total_nodes // 2)

    def _calculate_height(self, node):
        if node is None:
            return 0
        return 1 + self._calculate_height(node.left)
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
sum_of_nodes = tree.calculate_sum()
print("Sum of all nodes:", sum_of_nodes)
        

