# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        maxval = max(p.val , q.val)
        minval = min(p.val , q.val)
        while not(root.val <= maxval and root.val >= minval):
            if root.val > maxval:
                root = root.left
            if root.val < minval:
                root = root.right
        return root
            
        
                


        