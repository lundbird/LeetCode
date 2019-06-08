from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # return [x for x,y in Counter(nums).items() if y == 2]
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return res