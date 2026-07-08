def validate(node, low, high):
    if node is None:
        return True
    if not (low < node.val < high):
        return False
    return (
        validate(node.left, low, node.val) and
        validate(node.right, node.val, high)
    )
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return validate(root, float('-inf'), float('inf'))