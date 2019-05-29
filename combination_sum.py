class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort() #sorting allows us to prune uneeded paths
        res = []
        def dfs(target, path, index):
            if target == 0: 
                res.append(path)
                return
            for i in range(index, len(candidates)):
                if target-candidates[i] < 0: break
                dfs(target-candidates[i], path+[candidates[i]], i)
        
        dfs(target, [], 0)
        return res