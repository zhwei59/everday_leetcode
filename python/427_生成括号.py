class Solution:
    def gen(self,l,r,item):
        if l<r :
            return
        if l==0 and r==0:
            self.res.append(item)
        if l>0:
            self.gen(l-1,r,item+'(')
        if r>0:
            self.gen(l,r-1,item+')')
        return
    def generateParenthesis(self, n):
        if n<=0:
            return []
        self.res=[]
        self.gen(n,n,'')
        return self.res

