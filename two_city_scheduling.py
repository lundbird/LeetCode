class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = sorted([(x[1]-x[0],i) for i,x in enumerate(costs)])
        total = 0
        for i in range(len(diffs)//2):
            total += costs[diffs[i][1]][1]
        for i in range(len(diffs)//2,len(diffs)):
            total += costs[diffs[i][1]][0]
        return total