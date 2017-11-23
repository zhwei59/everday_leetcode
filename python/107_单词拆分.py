# -*- coding: UTF-8 -*-
class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    给出一个字符串s和一个词典，判断字符串s是否可以被空格切分成一个或多个出现在字典中的单词。


    dp[i]=dp[i] or (dp[i-j] and s[j:i+1] in dict)

    复杂度很大的解法
    def wordBreak(self, s, dict):
        # write your code here
        if not dict and not s:
            return True
        n=len(s)
        dp=[False for __ in range(n) ]
        for i in range(n):
            dp[i]=True if s[:i+1] in dict else False
            for j in range(i-1,-1,-1):
                dp[i]=dp[i] or (dp[j] and s[j+1:i+1] in dict)
        return dp[-1]



    """
    def wordBreak(self, s, dict):
        n = len(s)
        max_len = 0
        for e in dict:
            max_len = max(max_len, len(e))
        dp = [False for __ in range(n + 1)]
        dp[0] = True
        for i in range(1, n + 1):
            j = 1
            while j <= i and j <= max_len:
                if not dp[i - j]:
                    j += 1
                    continue
                if s[i - j:i] in dict:
                    dp[i] = True
                    break
                j += 1
        return dp[n]


