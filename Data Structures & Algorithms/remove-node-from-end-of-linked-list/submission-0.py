# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        prev=None
        while cur:
            tmp=cur.next
            cur.next=prev
            prev=cur
            cur=tmp
        rhead = prev
        if n !=1:
            for _ in range(n-2):
                prev=prev.next
            prev.next=prev.next.next
        else:
            rhead= prev.next
        cur = rhead
        prev = None
        while cur:
            tmp=cur.next
            cur.next=prev
            prev=cur
            cur=tmp
        return prev