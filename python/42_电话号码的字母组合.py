class Solution:
    def dfs(self,digits,s,n):
        if len(s)==n and s:
            self.res.append(s)
            return
        for i,c in enumerate(digits):
            cmap=self.ans[c]
            for a in cmap:
                self.dfs(digits[i+1:],s+a,n)
    def letterCombinations(self, digits):
        # write your code here
        self.ans = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        self.res=[]
        self.dfs(digits,'',len(digits))
        return self.res