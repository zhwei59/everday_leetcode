class Solution:
    """
    @param: s: A string
    @param: p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        # write your code here
        m=len(s)
        n=len(p)
        dp=[[False for __ in range(n+1)] for __ in range(m+1)]
        dp[0][0]=True
        for j in range(1,n+1):
            if p[j-1]=='*':
                dp[0][j]=dp[0][j-1]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1]=='*':
                    dp[i][j]=(dp[i][j-1] or dp[i-1][j])
                else:
                    if p[j-1]=='?' or s[i-1]==p[j-1]:
                        dp[i][j]=dp[i-1][j-1]
        return dp[m][n]
print Solution().isMatch('bbabacccbcbbcaaab','vewb')