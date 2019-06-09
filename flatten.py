class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None: return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            last_ptr = root.left
            while last_ptr.right:
                last_ptr = last_ptr.right
            last_ptr.right = root.right
            root.right = root.left
            root.left = None