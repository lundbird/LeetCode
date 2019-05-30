class Solution(object):
    def uniquePaths(self, r, c):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1]*c for row in range(r)]
        for i in range(1,r):
            for j in range(1,c):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]