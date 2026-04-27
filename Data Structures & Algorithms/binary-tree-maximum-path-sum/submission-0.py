# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max=-float("inf")
        def pathSum(root):
            if not root:
                return 0
            lmax=pathSum(root.left)
            rmax=pathSum(root.right)
            maxpath=max(lmax,rmax)
            if maxpath<=0:
                if root.val>self.max:
                    self.max=root.val
                return root.val
            else:
                realmax=max(maxpath,lmax+rmax)+root.val
                if realmax>self.max:
                    self.max =realmax
                return root.val+maxpath
        pathSum(root)
        return self.max