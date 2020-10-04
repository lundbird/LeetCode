class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(lambda: 0)
        majority = len(nums) // 2
        for item in nums:
            d[item] += 1
            if d[item] > majority:
                return item
        print("did not find majority element: " + str(nums))