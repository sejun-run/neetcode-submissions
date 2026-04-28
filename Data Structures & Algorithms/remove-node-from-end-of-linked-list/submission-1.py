# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        e=head
        dummy=ListNode()
        dummy.next=head
        s=dummy
        for i in range(n):
            e=e.next
        while e:
            s=s.next
            e=e.next
        after_n=s.next.next
        s.next=after_n
        return dummy.next