# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tail=head
        for _ in range(k-1):
            tail=tail.next if tail else None
        ftail=tail
        if not ftail:
            return head
        cur=head
        dummy=ListNode()
        f=None
        while tail:
            if f:
                f.next= tail
            f=cur
            prev=tail.next
            for _ in range(k):
                next=cur.next
                cur.next=prev
                prev=cur
                cur=next
                tail=tail.next if tail else None
        return ftail
        
            