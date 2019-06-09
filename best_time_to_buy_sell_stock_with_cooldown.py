class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []: return 0
        buy =[-prices[0]]*len(prices)
        sell =[float('-inf')]*len(prices)
        rest =[0]*len(prices)
        for i in range(1,len(prices)):
            rest[i] = max(rest[i-1],sell[i-1])
            buy[i] = max(buy[i-1],rest[i-1]-prices[i])
            sell[i] = buy[i-1]+prices[i]
        print(buy,rest,sell)
        return max(sell[-1],rest[-1])
        