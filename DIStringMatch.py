from collections import deque
class Solution:
    def diStringMatch(self, S: str):
        L, R = 0, len(S)
        A = range(len(S)+1)
        res = [None] * len(A)
        for i,c in enumerate(S):
            if c=="D":
                res[i] = A[R]
                R -= 1
            else:
                res[i] = A[L]
                L += 1
        res[-1] = A[L]
        return res

