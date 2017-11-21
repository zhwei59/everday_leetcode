# -*- coding: UTF-8 -*-
class Solution:
    """
    @param: A: A list of integers
    @return: A boolean

    给出一个非负整数数组，你最初定位在数组的第一个位置。　　　

数组中的每个元素代表你在那个位置可以跳跃的最大长度。　　　　

判断你是否能到达数组的最后一个位置。

 注意事项

这个问题有两个方法，一个是贪心和 动态规划。

贪心方法时间复杂度为O（N）。

动态规划方法的时间复杂度为为O（n^2）。

我们手动设置小型数据集，使大家可以通过测试的两种方式。这仅仅是为了让大家学会如何使用动态规划的方式解决此问题。如果您用动态规划的方式完成它，你可以尝试贪心法，以使其再次通过一次。
    """
    def greed(self,A):
        length=len(A)
        reach=0
        for i,c in enumerate(A):
            reach=max(reach,i+c)
            if reach>=length-1:
                return True
            if reach<=i and i<length-1:
                return False
    def dpf(self,A):
        length=len(A)
        h=set([])
        for i,c in enumerate(A):
            reach=i+c
            t=set([])
            t.add(reach)
            for j in h:
                if reach<j:
                    t.add(j)
                    reach=max(j,reach)
            if reach>=length-1:
                return True
            if reach<=i and i<length-1:
                return False
            h=t
    def canJump(self, A):
        self.greed(A)

