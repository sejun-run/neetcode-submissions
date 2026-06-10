"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyList={}
        def dfs(node: 'Optional[Node]') -> 'Optional[Node]':
            if not node:
                return None
            if node in copyList:
                return copyList[node]
            copyList[node]=Node(node.val)
            new_node=copyList[node]
            new_node.next=dfs(node.next)
            new_node.random=dfs(node.random)
            return new_node
        return dfs(head)
            
                