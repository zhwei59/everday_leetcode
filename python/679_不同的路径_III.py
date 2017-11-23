# -*- coding: UTF-8 -*-
class Solution:
    """
    @param: : an array of arrays
    @return: the sum of all unique weighted paths


    "不同的路径II"的 follow up:http://lintcode.com/en/problem/unique-paths-ii/
现在每一个格子都包含了一个值,所以每条路径都有一个值,找到所有值不同的路径的和

样例
举个例子,

[
  [1,1,2],
  [1,2,3],
  [3,2,4]
]
这里有两条值不同的路径:
[1,1,2,3,4] = 11
[1,1,2,2,4] = 10
返回 21


    """

    def uniqueWeightedPaths(self, grid):
        if not grid or not grid[0]:
            return 0
        m=len(grid)
        n=len(grid[0])
        dp=[[set([]) for i in range(n)] for __ in range(m)]
        curr=0
        for i  in range(m):
            curr+=grid[i][0]
            dp[i][0].add(curr)
        curr=0
        for j in range(n):
            curr+=grid[0][j]
            dp[0][j].add(curr)
        for i in range(1,m):
            for j in range(1,n):
                up=dp[i-1][j]
                left=dp[i][j-1]
                dp[i][j]=set(map(lambda x:x+grid[i][j], up.union(left)))
        return sum(dp[m-1][n-1])
