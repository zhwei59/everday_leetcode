# -*- coding: UTF-8 -*-
class Solution:
    """
    @param: m: An integer m denotes the size of a backpack
    @param: A: Given n items with size A[i]
    @param: V: Given n items with value V[i]
    @return: The maximum value

    完全背包问题
    def backPackII(self, m, A, V):
        # write your code here
        l = len(A)
        m_p=0
        dp = [[0 for __ in range(m + 1)] for __ in range(l)]
        for j in range(m):
            dp[0][j] = V[0]*(j/A[0])
        for i in range(1,l):
            for j in range(m+1):
                use=(j//A[i])*A[i]
                dp[i][j]=V[i]*(j//A[i])+dp[i-1][j-use]
                m_p=max(m_p,dp[i][j])
        return m_p
print Solution().backPackII(100,
[77,22,29,50,99],
[92,22,87,46,90])

    def backPackII(self, m, A, V):
        l=len(A)
        dp=[[0 for __ in range(m+1)] for __ in range(l)]
        for i in range(A[0],m+1):
            dp[0][i]=V[0]
        for i in range(1,l):
            for j in range(m+1):
                if j>=A[i]:
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-A[i]]+V[i])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]

    """


def backPackII(self, m, A, V):
    l=len(A)
    dp=[0 for i in range(m+1)]
    for i in range(l):
        for j in range(m,A[i]-1,-1):
            dp[j]=max(dp[j],dp[j-A[i]]+V[i])
    return dp[-1]



