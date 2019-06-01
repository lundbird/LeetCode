class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
                 h   o   r   s   e
            0    1   2   3   4   5 
        r   1    1   2   2   3   4
        o   2    2   1   2   3   4
        s   3    3   2   2   2   3
        
        """
        if word1=="" and word2=="": return 0 
        if word1=="": return len(word2)
        if word2=="": return len(word1)
        
        dp = [[None]*(len(word1)+1) for i in range(len(word2)+1)]
        for i in range(0,len(word1)+1):
            dp[0][i] = i
        for i in range(0,len(word2)+1):
            dp[i][0] = i
        print(dp)
        for i in range(1,len(word2)+1):
            for j in range(1,len(word1)+1):
                if word1[j-1] != word2[i-1]:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) +1
                else:
                    dp[i][j] = dp[i-1][j-1]
                    
        return dp[-1][-1]