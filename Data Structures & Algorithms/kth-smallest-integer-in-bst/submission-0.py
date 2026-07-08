# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder_recursive(root: TreeNode) -> list:
    res = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)       
        res.append(node.val) 
        dfs(node.right)      
    dfs(root)
    return res
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = inorder_recursive(root)
        return arr[k-1]

        

        
        


        

        