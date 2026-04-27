# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        if not root:
            return result
        queue= deque([root])
        
        while queue:
            sublist=[]
            for _ in range(len(queue)):
                node = queue.popleft()
                sublist.append(node.val)
                if node.left != None:            
                    queue.append(node.left)
                if node.right != None:            
                    queue.append(node.right)
            result.append(sublist)
        return result