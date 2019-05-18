class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        #create a new tree by doing level order traversal of first tree and reversing insert conditions
        #swap left and right of each node recursively
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
