# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        minorder=-1
        for i in range(len(inorder)):
            for p in range(len(preorder)):
                if inorder[i]== preorder[p]:
                    order=p
                    break
            print("order",i, order, minorder)
            if minorder<0 or order < minorder:
                minorder= order
                t=i
        print(t, minorder)
        root=TreeNode(inorder[t])
        if t>0:
            root.left = self.buildTree(preorder,inorder[:t])
        if t< len(inorder)-1:
            root.right = self.buildTree(preorder,inorder[t+1:])
        return root