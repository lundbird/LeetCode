class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        cur_max = 0
        for num in s:
            if num-1 in s:
                continue
            count = 0
            while num in s:
                count += 1
                num += 1
            cur_max = max(cur_max,count)
        return cur_max