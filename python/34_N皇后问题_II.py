class Solution:


    def dfs(self,i, jstack, n):
        if i == n:
            self.res += 1
            return
        if i>n:
            return
        for j in range(n):
            jstack[i] = j
            for k in range(i):
                if (jstack[k] == j or i + j == k + jstack[k] or  i - j == k - jstack[k]):
                    break
            else:
                self.dfs(i + 1, jstack, n)


    def totalNQueens(self, n):
        # write your code here
        self.res = 0
        jstack=[0 for __ in range(n)]
        self.dfs(0, jstack, n)
        return self.res
print Solution().totalNQueens(10)
