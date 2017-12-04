class Solution:
    def recursion(self,i,n):
        if i==n:
            return
        else:
            ng=[]
            rate=1
            for j in range(i):
                rate*=10
            for j in range(10):
                num=rate*j
                for k in self.res:
                    re=k+num
                    ng.append(re)
            self.res=ng
            self.recursion(i+1,n)
    def numbersByRecursion(self, n):
        # write your code here
        if n==0:
            return []
        self.res=[i for i in range(10)]
        self.recursion(1,n)
        return self.res[1:]
print Solution().numbersByRecursion(3)