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
        if m+n !=l:
            return False
        dp=[[False for __ in range(n+1)] for __ in range(m+1)]
        dp[0][0]=True
        for i in range(1,m+1):
            if s1[i-1]==s3[i-1]:
                dp[i][0]=True
        for j in range(1,n+1):
            if s2[j-1]==s3[j-1]:
                dp[0][j]==True
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j]= (dp[i-1][j] and s1[i-1]== s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
        return dp[m][n]
print Solution().isInterleave("","a","a")