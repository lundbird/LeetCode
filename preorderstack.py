class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None: return []
        stack = [root]
        visited = []
        while stack:
            node = stack.pop()
            visited.append(node.val)
            for child in node.children[::-1]:
                stack.append(child)
        return visited