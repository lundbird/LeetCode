# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node): #returns (val if choosing this node, val if not choosing this node)
            if node is None: return (0,0)
            left = dfs(node.left)
            right = dfs(node.right)
            # print(node.val+left[1]+right[1], max(left[0]+right[0],left[1]+right[1],left[0]+right[1],left[1]+right[0]))
            return (node.val+left[1]+right[1], max(left[0]+right[0],left[1]+right[1],left[0]+right[1],left[1]+right[0])) #vals can be negative
        return max(dfs(root))