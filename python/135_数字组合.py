class Solution:
    def combinationSum(self, candidates, target):
        candidates=list(set(candidates))
        candidates.sort()
        self.res=[]
        self.dfs(candidates,[],0,target)
        return self.res
    def dfs(self,nums,curr,start,target):
        if target==0:
            self.res.append(curr)
        if target <=0:
            return
        for i in range(start,len(nums)):
            self.dfs(nums,curr+[nums[i]],i,target-nums[i])

