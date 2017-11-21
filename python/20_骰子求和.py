class Solution:
    def dicesSum(self, n):
        dp=[[0 for __  in range(6*n+1) ] for __ in range(n+1)]
        for i in range(1,7):
            dp[1][i]=1.0/6.0
        for i in range(2,n+1):
            for j in range(i,6*n+1):
                for k in range(1,7):
                    if j>k:
                        dp[i][j]+=dp[i-1][j-k]
                dp[i][j]/=6.0
        res=[]
        for i in range(n,6*n+1):
            res.append((i,dp[n][i]))
        return res

