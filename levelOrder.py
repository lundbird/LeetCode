from collections import deque
class Solution(object):
    def levelOrder(self, root):
        if not root: return []
        res = []
        q = deque([(root,0)])
        last_depth = -1
        while q:
            node, depth = q.popleft()
            if node.left: 
                q.append((node.left,depth+1))
            if node.right: 
                q.append((node.right,depth+1))
            if depth != last_depth:
                last_depth = depth
                res.append([node.val])
            else:
                res[-1].append(node.val)
        return res