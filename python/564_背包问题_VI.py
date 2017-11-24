import  sys
class Solution:
    """
    @param: nums: an integer array and all positive numbers, no duplicates
    @param: target: An integer
    @return: An integer
    """

    def backPackVI(self, nums, target):
        dp=[0 for __ in range(target+1)]
        dp[0]=1
        for i in range(1,target+1):
            for a in nums:
                if i>=a:
                    dp[i]+=dp[i-a]
        return dp[target]

print Solution().backPackVI([37,40,28,39,36,20,23,25,31,1,2,3,4],31)