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
        cur=head
        while cur:
            copy=Node(cur.val)
            copylist[cur]=copy
            cur=cur.next
        cur=head
        while cur:
            copy=copylist[cur]
            copy.next=copylist[cur.next] if cur.next else None
            copy.random=copylist[cur.random] if cur.random else None
            cur=cur.next
        return copylist[head]