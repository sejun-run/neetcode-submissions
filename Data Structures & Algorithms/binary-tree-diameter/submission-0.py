# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if node is None:
                return [0,0]
            lh,ld=dfs(node.left)
            rh,rd=dfs(node.right)
            h=max(lh,rh)+1
            d=max(ld,rd,lh+rh)
            return [h,d]
        return dfs(root)[1]