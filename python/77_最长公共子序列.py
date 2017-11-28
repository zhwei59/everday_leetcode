class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        m=len(A)
        n=len(B)
        dp=[[0 for __ in range(m+1)] for __ in range(n+1)]
        for i in range(m+1):
            for j in range(n+1):
                dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
                if A[i]==B[j]:
                    dp[i+1][j+1]=dp[i][j]+1
        return dp[m][n]