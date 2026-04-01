class Solution:
    def invert(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        root.left, root.right = root.right, root.left
        
        self.invert(root.left)
        self.invert(root.right)
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)
        return root
