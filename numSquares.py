from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        """works but time limit exceeded
        """
        if n == 0: return 0
        visited = []
        q = deque([(n,0)])
        while q:
            val,depth = q.popleft()
            visited.append(val)
            max_square = int(val**.5)
            for i in range(1,max_square+1):
                child = val-i**2
                if child == 0:
                    return depth+1
                if child not in visited and child not in q and child>=0:
                    q.append((child,depth+1))
        return -1