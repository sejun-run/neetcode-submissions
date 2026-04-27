# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def identical(a,b):
            if a==None and b==None:
                return True
            elif a==None or b ==None:
                return False 
            elif a.val!=b.val:
                return False
            else:
                return identical(a.left, b.left) and identical(a.right,b.right)
        if root==None:
            return subRoot==None
        elif identical(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)