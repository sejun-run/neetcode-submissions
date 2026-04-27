# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root ==None:
            return True
        def highest(root):
            while root.right:
                root=root.right
            return root.val
        def lowest(root):
            while root.left:
                root = root.left
            return root.val
        if root.left and highest(root.left) >= root.val:
            return False
        if root.right and lowest(root.right) <= root.val:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)