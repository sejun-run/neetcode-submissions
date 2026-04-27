# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return 0
            ld=dfs(node.left)
            rd=dfs(node.right)
            if ld!=-1 and rd!=-1 and -1<= ld-rd and ld-rd<=1:
                return max(ld,rd)+1
            return -1
        ret=dfs(root)
        return True if ret!=-1 else False