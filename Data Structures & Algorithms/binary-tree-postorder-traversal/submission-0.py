# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)    # Left
            dfs(node.right)   # Right
            ans.append(node.val)  # Visit
        dfs(root)
        return ans
