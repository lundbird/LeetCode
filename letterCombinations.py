class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0: return []
        res = []
        m = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        def dfs(digits, cur_string):
            if len(digits)==0:
                res.append(cur_string)
                return
            for c in m[int(digits[0])]:
                dfs(digits[1:],cur_string+c)
        
        dfs(digits,'')
        return res
