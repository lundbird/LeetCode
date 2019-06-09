from collections import deque
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        q = deque([(root,0)])
        row_max = [root.val]
        last_d = 0
        while q:
            n, d = q.popleft()
            if n is None: continue
            if last_d == d:
                row_max[-1] = max(row_max[-1],n.val)
            else:
                row_max.append(n.val)
                last_d = d
            q.append((n.left,d+1))
            q.append((n.right,d+1))
        return row_max