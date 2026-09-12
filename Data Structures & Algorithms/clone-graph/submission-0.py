"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        created = {node : Node(node.val)}
        queue = deque([node])

        while queue:
            popped = queue.popleft()
            for neighbor in popped.neighbors:
                if neighbor not in created:
                    created[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                created[popped].neighbors.append(created[neighbor])
        return created[node]
