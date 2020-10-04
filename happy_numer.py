class Solution:
    def isHappy(self, n: int) -> bool:
        s = set([n])
        while True:
            n = sum([int(c)**2 for c in str(n)])            
            if n == 1:
                return True
            if n in s:
                return False
            s.add(n)