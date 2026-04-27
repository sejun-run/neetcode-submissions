# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def height(root):
            if not root:
                return 0
            return 1+max(height(root.left), height(root.right))
        ret=""
        queue=deque([root])
        while queue and len(queue)<2**height(root):
            node= queue.popleft()
            ret+= str(node.val)+','
            if node.left:
                queue.append(node.left)
            else:
                queue.append(TreeNode(''))
            if node.right:
                queue.append(node.right)
            else:
                queue.append(TreeNode(''))
        print(ret)
        return ret

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        datalist= data.split(',')
        def deserial(i):
            if i>= len(datalist):
                return None
            val=datalist[i]
            if val!='':
                node = TreeNode(val)
                node.left= deserial(i*2+1)
                node.right= deserial(i*2+2)
            else:
                return None
            return node
        return deserial(0)
