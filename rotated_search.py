class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        min_index = min(enumerate(nums),key=lambda x: x[1])[0]
        nums = nums[min_index:] + nums[:min_index]
        i = bisect.bisect_left(nums,target) 
        if i != len(nums) and nums[i]==target:
            return (i+min_index) % len(nums)  
        else:
            return -1
        