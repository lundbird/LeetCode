class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #idea sell at each valley and peak
        """
        right idea. solution is better because we dont have to worry about mismatched indices and two pointers. outer for loop with two while loops that find the valley :) #useful trick here is that you can keep using i to find the next peak after the valley and the next valley after that peak!
        """
        i,ans = 0,0
        while i < (len(prices)-1):
            while i<(len(prices)-1) and prices[i]>prices[i+1]:
                i += 1
            ans -= prices[i]
            while i<(len(prices)-1) and prices[i]<=prices[i+1]:
                i += 1
            ans += prices[i]
        return ans
            