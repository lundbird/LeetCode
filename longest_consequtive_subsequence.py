def longest_subsequence(A):
    dp = [A[0]]*len(A)
    for i in range(1,len(A)):
        dp[i] = max(dp[i-1]+A[i],A[i])
    return max(dp)


A=[-2, -3, 4, -1, -2, 1, 5, -3]
print(longest_subsequence(A))