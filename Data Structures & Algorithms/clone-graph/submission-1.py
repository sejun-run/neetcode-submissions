"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        newGraph={}
        if not node:
            return None
        def dfs(node: 'Node') -> 'Node':
            value=node.val
            if value in newGraph:
                return newGraph[value]
            else:
                newNode=Node(value)
                newGraph[value]=newNode
            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(neighbor))
            return newNode
        return dfs(node)
            