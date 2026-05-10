# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "n,"
        ret=str(root.val) + ','
        ret+=self.serialize(root.left)
        ret+=self.serialize(root.right)
        return ret

            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tree = [x for x in data.split(',') if x]
        self.i=0

        def dfs() -> Optional[TreeNode]:
            if tree[self.i]=='n':
                self.i+=1
                return None
            node=TreeNode(int(tree[self.i]))
            self.i+=1
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()
