from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = Counter(A[0])
        for i in range(1,len(A)):
            res &= Counter(A[i])
        return list(res.elements())