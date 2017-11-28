class Solution:
    """
    @param: nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums:
            return 0
        n=len(nums)
        dp=[1 for __ in range(n)]
        for i in range(1,n):
            curr=1
            for j in range(i):
                if nums[j]<nums[i]:
                    curr=max(curr,dp[j]+1)
            dp[i]=curr
        return max(dp)
