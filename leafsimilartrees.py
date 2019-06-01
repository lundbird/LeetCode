class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        def dfs(node, seq):
            if node is None: 
                return seq
            if node.left is None and node.right is None: 
                seq.append(node.val)
            else:
                dfs(node.left,seq)
                dfs(node.right,seq)
            return seq
        
        return dfs(root1,[])==dfs(root2,[])