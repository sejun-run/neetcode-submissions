# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(l,r):
            if not l and not r:
                return True
            if not l or not r or l.val!=r.val:
                return False
            return is_same(l.left,r.left) and is_same(l.right,r.right)
        queue=deque([root])
        while queue:
            node=queue.popleft()
            if not node:
                return not subRoot
            if node.val==subRoot.val:
                if is_same(node,subRoot):
                    return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False