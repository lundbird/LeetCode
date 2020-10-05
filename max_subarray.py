class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]*len(nums)
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1],0) + nums[i]
        return max(dp)