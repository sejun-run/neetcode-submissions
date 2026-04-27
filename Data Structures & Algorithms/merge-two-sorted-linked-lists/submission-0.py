# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or (list2 and list1.val>list2.val):
            head = list2
            cur= list1
        else:
            head = list1
            cur= list2
        
        main=head
        while main.next:
            while cur and main.next.val >= cur.val:
                next = main.next
                main.next = cur
                nextcur=cur.next
                cur.next= next
                main = cur
                cur=nextcur
            main= main.next
        main.next=cur
        return head
        