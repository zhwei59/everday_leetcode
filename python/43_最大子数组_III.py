# -*- coding: UTF-8 -*-
import sys
class Solution:
    """
    @param: nums: A list of integers
    @param: k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    经典的动态规划
    最重要的把握是，构造两个二维数组，一个必须包含i-1，一个不一定包含！
    这样就会好处理很多。
    """
    def maxSubArray(self, nums, k):
        n=len(nums)
        local=[[-sys.maxint for __ in range(k+1)] for __ in range(n+1)]
        globle=[[-sys.maxint for __ in range(k+1)] for __ in range(n+1)]
        for i in range(n+1):
            local[i][0]=globle[i][0]=0
        for i in range(1,n+1):
            for j in range(1,k+1):
                local[i][j]=max(local[i-1][j]+nums[i-1],globle[i-1][j-1]+nums[i-1])
                globle[i][j]=max(local[i][j],globle[i-1][j])
        return globle[n][k]