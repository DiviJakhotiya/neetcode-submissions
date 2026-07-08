# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        arr = []
        def populate(node):
            if node is None:
                arr.append("null")
                return
            arr.append(str(node.val))
            populate(node.left)
            populate(node.right)
        populate(root)
        return ",".join(arr)
                
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0
        def dfs():
            if vals[self.i] == "null":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i = self.i + 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
