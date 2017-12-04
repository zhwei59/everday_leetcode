class Solution:
    """
    [
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
    """
    def subsets(self,nums):
        res=[[]]
        nums.sort()
        for i in nums:
            pre=[]
            for s in res:
                pre.append(s+[i])
            res=res+pre
        return res

print Solution().subsets([0,1,2,3])