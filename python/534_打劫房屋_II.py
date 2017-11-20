# -*- coding: UTF-8 -*-
class Solution:
    """
    @param: nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    在上次打劫完一条街道之后，窃贼又发现了一个新的可以打劫的地方，但这次所有的房子围成了一个圈，这就意味着第一间房子和最后一间房子是挨着的。每个房子都存放着特定金额的钱。你面临的唯一约束条件是：相邻的房子装着相互联系的防盗系统，且 当相邻的两个房子同一天被打劫时，该系统会自动报警。

给定一个非负整数列表，表示每个房子中存放的钱， 算一算，如果今晚去打劫，你最多可以得到多少钱 在不触动报警装置的情况下。
给出nums = [3,6,4], 返回　6，　你不能打劫3和4所在的房间，因为它们围成一个圈，是相邻的．\

最大循环的间隔是i-3

单序列的dp。递推好找得很。
    """
    def houseRobber2(self, nums):
        if not nums:
            return 0
        length=len(nums)
        if length<=3:
            return max(nums)
        dp=[0 for __ in range(length)]
        dp[0]=nums[0]
        dp[1]=nums[1]
        dp[2]=max(nums[0]+nums[2],nums[1])
        for i in range(3,length):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i],dp[i-3]+nums[i])
        if dp[2]>dp[1]:
            return max(dp[-1]-min(nums[0],nums[-1]),dp[-2])
        else :
            return dp[-1]
