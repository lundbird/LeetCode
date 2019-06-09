class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def is_same_tree(leftchild,rightchild):
            if leftchild==None and rightchild==None:
                return True
            if leftchild==None or rightchild==None:
                return False
            if leftchild.val!=rightchild.val:
                return False
            outer = is_same_tree(leftchild.left,rightchild.right)
            inner = is_same_tree(leftchild.right,rightchild.left)
            return outer and inner
        
        return is_same_tree(root.left,root.right) if root else True