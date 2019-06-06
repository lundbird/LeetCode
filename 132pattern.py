class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        for j in range(1,len(nums)-1):
            min_left = min(nums[:j])
            if min_left >= nums[j]:
                continue
            for k in range(j+1,len(nums)):
                if min_left < nums[k] < nums[j]:
                    return True
        return False