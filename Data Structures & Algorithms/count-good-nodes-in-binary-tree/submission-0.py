# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ret=0
        def dfs(cur,cmax):
            if cur.val >= cmax:
                self.ret+=1
                cmax=cur.val
            if cur.left:
                dfs(cur.left,cmax)
            if cur.right:
                dfs(cur.right,cmax)
        dfs(root,root.val)
        return self.ret