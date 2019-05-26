class Solution(object):
    def inorderTraversalRecursive(self, root):
        def traverse(node):
            if node is None: return
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
        result = []
        traverse(root)
        return result
    
    def inorderTraversalIterative(self,root):
        #need to use two while loops, one to add all left values onto stack.
        stack, res = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res