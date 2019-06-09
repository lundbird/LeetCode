class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_end, max_diff = 0, 0
        for i in reversed(range(len(prices))):
            max_end = max(max_end, prices[i])
            max_diff = max(max_end - prices[i], max_diff)
        return max_diff