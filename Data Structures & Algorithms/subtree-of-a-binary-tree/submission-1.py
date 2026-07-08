def dfs(a, b):
    if not a and not b:
        return True
    if not a or not b:
        return False
    if a.val != b.val:
        return False

    return dfs(a.left, b.left) and dfs(a.right, b.right)

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if dfs(root, subRoot):
            return True
        return (
            self.isSubtree(root.left, subRoot)
            or
            self.isSubtree(root.right, subRoot)
        )
        
        
        