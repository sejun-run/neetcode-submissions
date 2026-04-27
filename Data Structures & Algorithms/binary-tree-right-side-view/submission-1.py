# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ret=[]
        queue=deque([root])
        ret.append(root.val)
        while queue:
            nqueue=[]
            for i in range(len(queue)):
                node=queue.popleft()
                if node.left:
                    nqueue.append(node.left)
                if node.right:
                    nqueue.append(node.right)
            for n in nqueue:
                print(n.val)
            print('')
            if not nqueue:
                return ret
            rightnode=nqueue[-1]
            queue=deque(nqueue)
            ret.append(rightnode.val)
        return ret    
            