
# from functools import lru_cache
# @lru_cache(maxsize=None)
def maxCoins(nums):
    if len(nums)==1: 
        return nums[0]
    res = []
    res.append(maxCoins(nums[1:]))
    for i in range(1,len(nums)-1):
        res.append(maxCoins(nums[:i]+nums[i+1:]))
    res.append(maxCoins(nums[:len(nums)-1]))
    print(res)
    return max(res)

print(maxCoins(tuple([3,1,5,8])))