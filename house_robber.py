def rob(self, nums: List[int]) -> int:
    T = nums
    if not T: return 0
    if len(T) < 3: return max(T)
    T[1] = max(T[0],T[1])
    for i in range(2,len(nums)):
        T[i] = max(T[i-1], T[i-2]+nums[i])
    return T[-1]