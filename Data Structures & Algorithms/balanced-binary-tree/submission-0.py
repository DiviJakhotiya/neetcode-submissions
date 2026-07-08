# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dfs(node):
    if not node:
        return 0
    return 1 + max(dfs(node.left), dfs(node.right))
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
            if root is None:
                return True
            
            leftnode = dfs(root.left)
            rightnode = dfs(root.right)
            if abs(leftnode - rightnode) > 1:
                return False
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        