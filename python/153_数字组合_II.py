class Solution:
    """
    @param: num: Given the candidate numbers
    @param: target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        num.sort()
        self.res=[]
        self.dfs(num,[],target,0)
        return self.res
    def dfs(self,num,curr,target,start):
        if target==0:
            self.res.append(curr)
        if target<=0:
            return
        n=len(num)
        i=start
        while i<n:
            self.dfs(num,curr+[num[i]],target-num[i],i+1)
            while i+1<n and  num[i]==num[i+1]:
                i+=1
            i+=1