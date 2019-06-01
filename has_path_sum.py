class Solution(object):
    def hasPathSum(self, root, sum):
        if root is None: return False #on these problems ALWAYS think of base
        sum -= root.val 
        if root.left is None and root.right is None:
            if sum == 0: 
                return True
            else:
                return False
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right, sum)