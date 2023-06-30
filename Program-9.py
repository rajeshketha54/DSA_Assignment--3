# Find maximum level sum in Binary Tree
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    def max_level_sum(self):
        if self.root is None:
            return 0
        max_sum = float("-inf")
        max_level = 0
        level = 1
        queue = deque()
        queue.append(self.root)
        while queue:
            level_sum = 0
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.data
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            level += 1
        return max_level, max_sum
        
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.right = Node(8)
tree.root.right.right.left = Node(6)
tree.root.right.right.right = Node(7)
max_level, max_sum = tree.max_level_sum()
print("Maximum level sum found at level", max_level, "with a sum :", max_sum)
