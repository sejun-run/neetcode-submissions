# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        t= inorder.index(preorder[0])
        root=TreeNode(inorder[t])
        if t>0:
            root.left = self.buildTree(preorder[1:1+t],inorder[:t])
        if t< len(inorder)-1:
            root.right = self.buildTree(preorder[t+1:],inorder[t+1:])
        return root