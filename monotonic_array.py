class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        # return A==sorted(A,reverse=True) or  A==sorted(A)
        if len(A)<2: return True
        isIncreasing = False
        if A[-1]>A[0]:
            isIncreasing = True
        if isIncreasing:
            for i in range(len(A)-1):
                if (A[i+1] < A[i]):
                    return False
        else:
            for i in range(len(A)-1):
                if (A[i+1] > A[i]):
                    return False
        return True