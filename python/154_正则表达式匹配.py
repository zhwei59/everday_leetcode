# -*- coding: UTF-8 -*-
class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """

    def isMatch(self, s, p):
        # write your code here
        n=len(p)
        m=len(s)
        dp = [[False for i in range(0, n+1)] for j in range(0, m+1)]
        dp[0][0] = True
        for i in range(1, n+1):
            if (p[i - 1] == '*'):
                dp[0][i] = dp[0][i - 2]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] |= dp[i - 1][j]
                else:
                    if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]


print Solution().isMatch("aa",".*")
print Solution().isMatch("aa","aa")
print Solution().isMatch("bbbba",".*a*a")
print Solution().isMatch("aab","c*a*b")
print Solution().isMatch("acaabbaccbbacaabbbb","a*.*b*.*a*aa*a*")
