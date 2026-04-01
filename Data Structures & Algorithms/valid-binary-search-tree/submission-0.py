# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root: Optional[TreeNode], min_val: int, max_val: int) -> bool:
            if not root:
                return True
            if min_val >= root.val or max_val <= root.val:
                return False
            return validate(root.left, min_val, root.val) and validate(root.right, root.val, max_val)
        
        return validate(root, float('-inf'), float('inf'))
