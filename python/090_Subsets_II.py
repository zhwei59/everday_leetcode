class Solution(object):
    def subsetsWithDup(self, nums):
        """
        Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
       Note: The solution set must not contain duplicate subsets.
       For example,
      If nums = [1,2,2], a solution is:
     [
    [2],
    [1],
    [1,2,2],
    [2,2],
    [1,2],
    []]
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[[]]

        nums.sort()
        tmp_size=0
        for i in range(len(nums)):
            start=tmp_size if i>=0 and nums[i]==nums[i+1] else 0
            length = len(res)
            for j in range(tmp_size,length):
                res.append(res[j]+[nums[i]])
        return res





