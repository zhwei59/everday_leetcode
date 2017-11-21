class Solution:
    """
    @param: obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0 for __ in range(n)] for i in range(m)]
        for i in range(m):
            if obstacleGrid[i][0]==0:
                dp[i][0]=1
            else :
                break
        for j in range(n):
            if obstacleGrid[0][j]==0:
                dp[0][j]=1
            else:
                break
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1] if obstacleGrid[i][j]==0 else 0
        return dp[m-1][n-1]