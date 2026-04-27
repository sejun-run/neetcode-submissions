"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        dupmap={}
        def dfs(node):
            val=node.val
            neighbors=node.neighbors
            dupmap[val]=Node(val)
            for i in range(len(neighbors)):
                nnode=neighbors[i]
                if not dupmap.get(nnode.val,None):
                    nnode=neighbors[i]
                    dfs(nnode)
                dupmap[val].neighbors.append(dupmap[nnode.val])
        dfs(node)
        return dupmap[1]
        
                