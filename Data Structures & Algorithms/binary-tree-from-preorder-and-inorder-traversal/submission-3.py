# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        order={}
        for i, n in enumerate(preorder):
            order[n]=i
        def parseTree(start,end):
            minord=None
            for i in range(start,end+1):
                if minord is None or minord>order[inorder[i]]:
                    minidx=i
                    minord=order[inorder[i]]
            root=TreeNode(inorder[minidx])
            if start<minidx:
                root.left=parseTree(start,minidx-1)
            if minidx<end:
                root.right=parseTree(minidx+1,end)
            return root
        return parseTree(0,len(inorder)-1)