class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = Counter(nums1) & Counter(nums2)
        result = []
        for k,v in intersection.items():
            result.extend([k]*v)
        return result        

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:  
        res = []
        for k in nums1:
            if k in nums2:
                res.append(k)
                nums2.remove(k)
        return res
        