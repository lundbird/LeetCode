from collections import Counter
#one liner
class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        #use the Counter built in type
        return Counter(nums).most_common()[-1][0]

    def singleNumber2(self, nums: List[int]) -> int:
        #use the defaultdictionary with default value of 0
        counts = defaultdict(lambda:0)
        for val in nums:
            counts[val] += 1
        for k,v in counts.items():
            if (v==1):
                return k

    def singleNumber3(self, nums: List[int]) -> int:
        #append if not in list, delete if in list. O(n^2)
        counts = []
        for val in nums:
            if val not in counts:
                counts.append(val)
            else:
                counts.remove(val)
        return counts.pop()
    
    def singleNumber4(self, nums: List[int]) -> int:
        #same as above but use sets which is implemented as hashtable. O(n)
        s = set()
        for val in nums:
            if val not in s:
                s.add(val)
            else:
                s.remove(val)
        return s.pop()

    def singleNumber5(self, nums: List[int]) -> int:
        #crazy fast. a xor a = 0 so xor everything is just the one left over
        a = 0
        for i in nums:
            a ^= i
        return a
