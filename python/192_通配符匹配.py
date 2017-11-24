class Solution:
    """
    @param: s: A string
    @param: p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        # write your code here
        if not s:
            return not p
        m=len(s)
        n=len(p)
        dp=[False for i in range(m+1)]
        dp[0]=True
        for j in range(1,n+1):
            pre=dp[0]
            dp[0]= dp[0] and p[j-1]=='*'
            for i in range(1,m+1):
                tmp=dp[i]
                if p[j-1] !='*':
                    dp[i]=pre and (s[i-1]==p[j-1] or p[j-1]=='?')
                else :
                    dp[i]=dp[i-1] or dp[i]
                pre=tmp
        return dp[m]



print Solution().isMatch('bbabacccbcbbcaaab','*a*b??b*b')