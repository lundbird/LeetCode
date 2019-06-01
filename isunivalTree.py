class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def dfs(node,val):
            if node is None: return True
            if node.val != val: return False
            left = dfs(node.left,val)
            right = dfs(node.right,val)            
            return left and right
        return dfs(root,root.val)