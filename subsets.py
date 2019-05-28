from itertools import compress
class Solution(object):
    
    def subsets(self, nums):
        res = set()
        bit_int = 2**len(nums)
        T_vec = [0] * len(nums)
        for i in range(bit_int):
            for j in range(len(nums)):
                T_vec[j] = self.getBit(i,j)
            res.add(tuple(compress(nums,T_vec)))
        return res
        
    def getBit(self, num, i):
        return ((num & (1<<i)) != 0)