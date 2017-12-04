class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = [[]]
        i = 0
        while i < len(nums):
            curr = []
            for s in res:
                curr.append(s + [nums[i]])
            res = res + curr
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                ducurr = []
                for s in curr:
                    ducurr.append(s + [nums[i]])
                curr = ducurr
                res = res + curr
                i += 1
            i += 1
        return res