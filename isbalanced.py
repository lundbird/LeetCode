# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:        
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node,depth):
            if not node: return depth
            left = dfs(node.right,depth)
            right = dfs(node.left,depth)
            if abs(left-right)>1: 
                nonlocal same_depth
                same_depth = False
            return max(left,right)+1
        same_depth = True
        dfs(root,0)
        return same_depth
            
            