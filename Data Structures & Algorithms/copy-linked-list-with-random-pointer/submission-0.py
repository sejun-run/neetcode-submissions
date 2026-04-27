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
        copylist={}
        def cp(cur):
            if not cur:
                return None
            copy=Node(cur.val)
            copylist[cur]=copy
            copy.next=cp(cur.next)
            copy.random=copylist[cur.random] if cur.random else None
            return copy
        return cp(head)