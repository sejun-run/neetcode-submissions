# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        left=deque([p])
        right=deque([q])
        while left and right:
            if len(left)!=len(right):
                return
            l=left.pop()
            r=right.pop()
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            left.append(l.left)
            left.append(l.right)
            right.append(r.left)
            right.append(r.right)
        return True