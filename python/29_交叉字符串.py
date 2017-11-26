class Solution:
    """
    @param: s1: A string
    @param: s2: A string
    @param: s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    s3=s1+s2
    """

    def isInterleave(self, s1, s2, s3):
        m=len(s1)
        n=len(s2)
        l=len(s3)
        if n+m!=l:
            return False
        dp=[True for __ in range(m+1)]
        for i in range(m):
            dp[i+1]=dp[0] and s1[i]==s3[i]

        for j in range(n):
            dp[0]=dp[0] and s2[j]==s3[j]
            for i in range(m):
                dp[i+1]=(dp[i] and s1[i]==s3[i+j+1]) or (dp[i+1] and s2[j]==s3[i+j+1])
        return dp[m]
