class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #brute force
        # out = []
        # for i in range(len(nums)):
        #     prod = 1
        #     for val in nums[:i]:
        #         prod *= val
        #     for val in nums[i+1:]:
        #         prod *= val
        #     out.append(prod)
        # return out
        L, R = [1]*len(nums), [1]*len(nums)
        for i in range(1,len(nums)):
            L[i] = nums[i-1]*L[i-1]
        for i in range(len(nums)-2,-1,-1):
            R[i] = nums[i+1]*R[i+1]
        return [L[i]*R[i] for i in range(len(nums))]