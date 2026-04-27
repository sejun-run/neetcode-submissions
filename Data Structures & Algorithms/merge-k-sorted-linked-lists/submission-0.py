# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head= None
        while True:
            min = None
            ml =-1
            for i in range(len(lists)):
                if lists[i] and (ml==-1 or lists[ml].val > lists[i].val):
                    ml=i
            if ml!=-1:
                if not head:
                    head= lists[ml]
                    cur = head
                else:
                    cur.next=lists[ml]
                    cur=lists[ml]
                lists[ml]=lists[ml].next
            else:
                break
        return head