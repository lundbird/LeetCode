class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(amount: int) -> int:
            if amount < 0:
                return math.inf
            if amount == 0:
                return 0
            changes = [1+dfs(amount-coin) for coin in coins]
            return min(changes)
        res = dfs(amount)
        return res if res != math.inf else -1
          # 0 1 2 3 4 5 6 7 8 9 10 11
          # 0 1 1 2 2 3 3 4 4 5 5  6
          # 0 1 1 2 2 1 2 2 3 3 2  3
          # dp[c] = min(dp[c-coin],dp[c])
        # dp = [math.inf] * (amount+1)
        # dp[0] = 0
        # for coin in coins:
        #     for x in range(coin,amount+1):
        #         dp[x] = min(dp[x], dp[x-coin] + 1)
        # return dp[-1] if dp[-1] != math.inf else -1
        
        
        