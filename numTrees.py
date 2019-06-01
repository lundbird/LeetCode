class Solution(object):
    def numTrees(self, n):
        G = [0]*(n+1)
        G[0] = G[1] = 1
        """
        G[n] = sum over i F(i,n)
        F(i,n) = G(i-1) *G(n-i)
        G(4) = F(1,4)+F(2,4)+F(3,4)+F(4,4) 
             = G0*G3 +G1*G2 +G2*G1 +G3*G0
             =G0*GN-1 + G1*GN-2 + G2*GN-3 + G3 * G0
        """
        for i in range(2,n+1):
            for j in range(i):
                G[i] += G[j]*G[i-j-1]
        return G[-1]