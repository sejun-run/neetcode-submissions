# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        bst=[]
        def toArray(root):
            if root.left:
                toArray(root.left)
            bst.append(root.val)
            if root.right:
                toArray(root.right)
        toArray(root)
        return bst[k-1]