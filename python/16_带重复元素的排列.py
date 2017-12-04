class Solution:
    def p(self,nums,curr,n):
        if n==0:
            self.res.append(curr)
            return
        else:
            i=0
            while i<len(nums):
                self.p(nums[:i]+nums[i+1:],curr+[nums[i]],n-1)
                while i+1<len(nums) and nums[i]==nums[i+1]:
                    i+=1
                i+=1

    def permuteUnique(self, nums):
        self.res=[]
        nums.sort()
        self.p(nums,[],len(nums))
        return self.res
