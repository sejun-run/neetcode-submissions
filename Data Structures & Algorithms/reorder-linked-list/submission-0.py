# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        array=[]
        cur=head
        while cur:
            array.append(cur)
            cur=cur.next
        n=len(array)
        if n%2==0:
            for k in range(n//2):
                array[k].next=array[n-k-1]
                if k!= n//2-1:
                    array[n-k-1].next=array[k+1]
                else:
                    array[n-k-1].next=None
        if n%2==1:
            for k in range(n//2):
                array[k].next=array[n-k-1]
                array[n-k-1].next=array[k+1]
            array[n//2].next=None