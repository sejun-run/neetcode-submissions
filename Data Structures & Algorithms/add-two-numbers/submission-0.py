# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        fcur=l1
        scur=l2
        fnum=fi=0
        snum=si=0
        while fcur:
            fnum+=fcur.val*(10**fi)
            fcur=fcur.next
            fi+=1
        while scur:
            snum+=scur.val*(10**si)
            scur=scur.next
            si+=1
        ret=fnum+snum
        def create(val):
            if val==0:
                return None
            cur=ListNode(val%10)
            cur.next=create(val//10)
            return cur
        return create(ret)