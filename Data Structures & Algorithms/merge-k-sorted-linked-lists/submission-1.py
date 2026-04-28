# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=ListNode()
        cur=dummy
        while True:
            next_node, li_num = None, None
            for n, li in enumerate(lists):
                if li and (next_node is None or next_node.val > li.val):
                    next_node=li
                    li_num=n
            if li_num is None:
                return dummy.next
            lists[li_num]=next_node.next
            cur.next=next_node
            cur=next_node
        raise Exception
            