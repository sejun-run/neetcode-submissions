# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.prior={}
        if len(self.prior)==0:
            for p in range(len(preorder)):
                self.prior[preorder[p]]=p
        minorder=-1
        for i in range(len(inorder)):
            if minorder<0 or self.prior[inorder[i]] < minorder:
                minorder= self.prior[inorder[i]]
                t=i
        print(t, minorder)
        root=TreeNode(inorder[t])
        if t>0:
            root.left = self.buildTree(preorder,inorder[:t])
        if t< len(inorder)-1:
            root.right = self.buildTree(preorder,inorder[t+1:])
        return root