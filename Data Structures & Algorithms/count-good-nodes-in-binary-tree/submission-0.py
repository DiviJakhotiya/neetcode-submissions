# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def function(node, pathmax):
    if node is None:
        return 0
    count = 1 if node.val >= pathmax else 0
    pathmax = max(pathmax, node.val)
    count += function(node.left, pathmax)
    count += function(node.right, pathmax)
    
    return count
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return function(root, root.val)
        
        