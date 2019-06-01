class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None: return 0
        max_child = 0
        for child in root.children:
            max_child = max(max_child, self.maxDepth(child))
        return max_child+1
    
    def maxDepth2(self, root: 'Node') -> int:
        if root is None: return 0
        stack = [(root,0)]
        max_found_depth = 0
        while stack:
            node, node_depth = stack.pop()
            max_found_depth = max(max_found_depth, node_depth)
            for child in node.children:
                stack.append((child, node_depth+1))
        return max_found_depth+1