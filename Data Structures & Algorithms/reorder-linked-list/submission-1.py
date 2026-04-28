# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s=f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        prev=None
        while s:
            temp=s.next
            s.next=prev
            prev=s
            s=temp
        org=head
        rev=prev
        while org and rev:
            orgtemp=org.next
            revtemp=rev.next
            org.next=rev
            rev.next=orgtemp if rev.next else None
            org, rev= orgtemp, revtemp