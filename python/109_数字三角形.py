# -*- coding: UTF-8 -*-
class Solution:
    """
    @param: triangle: a list of lists of integers
    @return: An integer, minimum path sum
    并没有用额外的空间
    """
    def minimumTotal(self, triangle):
        # write your code here
        n=len(triangle)
        for i in range(1,n):
            p=triangle[i-1]
            for j in range(1,i):
                triangle[i][j]+=min(p[j],p[j-1])
            triangle[i][0]+=p[0]
            triangle[i][-1]+=p[-1]
        return min(triangle[-1])
Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])