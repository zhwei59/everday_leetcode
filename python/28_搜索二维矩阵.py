class Solution:
    """
    @param: matrix: matrix, a list of lists of integers
    @param: target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix :
            return False
        m,n=len(matrix),len(matrix[0])
        left,right=0,m*n-1
        while left+1<right:
            mid=(left+right)/2
            x,y=mid/n,mid%n
            if matrix[x][y]<target:
                left=mid
            else :
                right=mid
        x,y=left/n,left%n
        if matrix[x][y]==target:
            return True
        x,y=right/n,right%n
        return matrix[x][y]==target