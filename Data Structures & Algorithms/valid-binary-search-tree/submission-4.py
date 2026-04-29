# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isInRange(start,end,node):
            if not node:
                return True
            if not start<node.val<end:
                return False
            new_end=node.val
            left = isInRange(start,new_end,node.left)
            new_start=node.val
            right = isInRange(new_start,end,node.right)
            return left and right
        return isInRange(-float('inf'),float('inf'),root)
        