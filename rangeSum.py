class Solution(object):
    def rangeSumBST(self, root, L, R):
        if root is None:
            return 0
        if root.val < L:
            return self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            return self.rangeSumBST(root.left, L, R)
        else:
            return self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R) + root.val