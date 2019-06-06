class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_A, sum_B = sum(A), sum(B)
        set_B = set(B)
        for a_val in A:
            b_val = (sum_B-sum_A)//2 + a_val
            if b_val in set_B:
                return [a_val,b_val]      