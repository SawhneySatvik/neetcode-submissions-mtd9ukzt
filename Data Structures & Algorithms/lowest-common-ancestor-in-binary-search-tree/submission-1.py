# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while True:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            elif (root.val > p.val and root.val < q.val) or (root.val > q.val and root.val < p.val):
                return root
            else:
                if root.val == p.val:
                    return p
                elif root.val == q.val:
                    return q
        