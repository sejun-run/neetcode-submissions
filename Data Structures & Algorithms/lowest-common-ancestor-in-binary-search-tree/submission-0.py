# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if q.val<p.val:
            q.val,p.val=p.val,q.val

        queue = deque([root])
        while queue:
            node=queue.popleft()
            if p.val<=node.val and node.val <=q.val:
                return node
            else:
                queue.append(node.left)
                queue.append(node.right)
        return False
            