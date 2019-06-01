class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        #works but isnt the cleanest. wont work if costs != 3
        spans = [1,7,30]
        days_set = set(days)
        T = [0 for i in range(days[-1]+1)]
        for r in range(len(costs)):
            for c in range(1,len(T)):
                if c not in days_set: #strictly better to wait so pull in last value
                    T[c] = T[c-1]
                else:
                     #clever way to check for OOB by using max here.
                    T[c] = min(T[max(c-30,0)]+costs[2],T[max(c-7,0)]+costs[1],T[max(c-1,0)]+costs[0])
        return T[-1]