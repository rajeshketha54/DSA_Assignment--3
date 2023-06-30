# Implement BFS (Breath First Search) and DFS (Depth First Search)
from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def bfs(self):
        if self.root is None:
            return

        queue = deque()
        queue.append(self.root)

        while queue:
            node = queue.popleft()
            print(node.data, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def dfs(self):
        if self.root is None:
            return

        stack = []
        stack.append(self.root)

        while stack:
            node = stack.pop()
            print(node.data, end=" ")

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("BFS traversal:",end=" ")
tree.bfs()
print("\n")
print("DFS traversal:",end=" ")
tree.dfs()

