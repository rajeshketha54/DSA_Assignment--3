# Find sum of all left leaves in a given Binary Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def sum_left_leaves(self):
        return self._sum_left_leaves_recursive(self.root, False)

    def _sum_left_leaves_recursive(self, node, is_left):
        if node is None:
            return 0

        if node.left is None and node.right is None and is_left:
            return node.data

        left_sum = self._sum_left_leaves_recursive(node.left, True)
        right_sum = self._sum_left_leaves_recursive(node.right, False)

        return left_sum + right_sum
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

sum_left = tree.sum_left_leaves()
print("Sum of all left leaves:", sum_left)
        
