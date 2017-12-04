class Solution:
    def p(self,nums,curr,n):
        if(n==0):
            self.res.append(curr)
            return
        else:
            for j in range(len(nums)):
                self.p(nums[:j]+nums[j+1:],curr+[nums[j]],n-1)
    def permute(self, nums):
        self.res=[]
        self.p(nums,[],len(nums))
        return self.res
