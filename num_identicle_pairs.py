def numIdenticalPairs(self, nums: List[int]) -> int:        
    sorted_nums = sorted(nums)
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if sorted_nums[i] == sorted_nums[j]:
                count += 1
            else:
                break
    return count