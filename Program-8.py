# Count subtress that sum up to a given value x in a binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def count_subtrees_with_sum(self, target_sum):
        count = self._count_subtrees_with_sum_recursive(self.root, target_sum)
        return count

    def _count_subtrees_with_sum_recursive(self, node, target_sum):
        if node is None:
            return 0

        count = 0
        if self._is_subtree_sum(node, target_sum):
            count += 1
        count += self._count_subtrees_with_sum_recursive(node.left, target_sum)
        count += self._count_subtrees_with_sum_recursive(node.right, target_sum)
        return count

    def _is_subtree_sum(self, node, target_sum):
        if node is None:
            return False

        if node.left is None and node.right is None:
            return node.data == target_sum
        left_sum = self._get_subtree_sum(node.left)
        right_sum = self._get_subtree_sum(node.right)
        return (left_sum + right_sum + node.data) == target_sum

    def _get_subtree_sum(self, node):
        if node is None:
            return 0
        return self._get_subtree_sum(node.left) + self._get_subtree_sum(node.right) + node.data
        
tree = BinaryTree()
tree.root = Node(5)
tree.root.left = Node(-3)
tree.root.right = Node(7)
tree.root.left.left = Node(2)
tree.root.left.right = Node(6)
tree.root.right.left = Node(1)
tree.root.right.right = Node(4)
target_sum = 7
count = tree.count_subtrees_with_sum(target_sum)
print("Number of subtrees with sum", target_sum, ":", count)
