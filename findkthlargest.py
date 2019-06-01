class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #track the len-k largest elements in an array. With k=0 this is max with k=len this is insertion sort
        arr = sorted(nums[:k])
        for i,val in enumerate(nums[k:]):
            if val < arr[0]:
                continue
            else:
                #insert val into the correct location
                for j in range(k):
                    if arr[j]>=val:
                        arr.insert(j,val)
                        del(arr[0])
                        break
        print(arr)
        return arr[0]