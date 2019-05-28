class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for r in range(len(A)-2,-1,-1):
            A[r][0] += min(A[r+1][0],A[r+1][1])
            for c in range(1,len(A[0])-1):
                A[r][c] += min(A[r+1][c-1],A[r+1][c],A[r+1][c+1])
            A[r][len(A[0])-1] += min(A[r+1][len(A[0])-2],A[r+1][len(A[0])-1])
        return min(A[0])