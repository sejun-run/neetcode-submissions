# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur= head
        nodeset=set()
        while cur and cur.next:
            nodeset.add(cur)
            if cur.next in nodeset:
                return True
            cur=cur.next
        return False
        