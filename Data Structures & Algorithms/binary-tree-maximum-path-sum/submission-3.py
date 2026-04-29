# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ret=-float('inf')
        def maxSum(node):
            sum=left=right=0
            if node.left and maxSum(node.left)>0:
                left=maxSum(node.left)
            if node.right and maxSum(node.right)>0:
                right=maxSum(node.right)
            self.ret=max(self.ret,node.val+left+right)
            return node.val+max(left,right)
        maxSum(root)
        return self.ret
        