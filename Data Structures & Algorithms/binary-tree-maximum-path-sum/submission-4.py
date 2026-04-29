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
            if node.left:
                left=max(left,maxSum(node.left))
            if node.right:
                right=max(right,maxSum(node.right))
            self.ret=max(self.ret,node.val+left+right)
            return node.val+max(left,right)
        maxSum(root)
        return self.ret
        