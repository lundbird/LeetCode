import re
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if s=="": return 1
        res = 0
        zero_ones = [m.start() for m in re.finditer('01', s)]
        res += len(zero_ones)
        one_zeros = [m.start() for m in re.finditer('10', s)]
        res += len(one_zeros)
        
        for pivot in zero_ones:
            l,r = pivot-1,pivot+2
            while l>=0 and r<len(s) and s[l]=="0" and s[r]=="1":
                res += 1
                l,r = l-1,r+1
                
        for pivot in one_zeros:
            l,r = pivot-1,pivot+2
            while l>=0 and r<len(s) and s[l]=="1" and s[r]=="0":
                res += 1
                l,r = l-1,r+1
                
        return res