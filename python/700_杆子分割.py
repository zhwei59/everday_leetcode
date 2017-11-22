# -*- coding: UTF-8 -*-
class Solution:
    """
    @param: : the prices
    @param: : the length of rod
    @return: the max value
    经典动态规划。
    dp[i]表示 杆子长度为i的最优
    达到的所有可能
    [1~i/2+1]
    """

    def cutting(self, prices, n):
        # Write your code here
        dp=[0 for __ in range(n+1)]
        for i in range(1,n+1):
            curr=prices[i-1]
            for j in range(1,i/2+1):
                curr=max(curr,dp[j]+dp[i-j])
            dp[i]=curr
        return dp[n]
Solution().cutting([3,5,8,9,10,17,17,20],8)