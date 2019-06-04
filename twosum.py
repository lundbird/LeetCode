    def twoSum(self, nums, target):
        dict = {}
        for i,val in enumerate(nums):
            if val in dict:
                return (dict[val],i)
            dict[target-val] = i