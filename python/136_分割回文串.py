class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def dfs(self,sub,curr):
        if len(sub)==0 and curr:
            self.res.append(curr)
            return
        else :
            for i in range(len(sub)):
                cstring=sub[:i+1]
                if self.isRecu(cstring):
                    self.dfs(sub[i+1:],curr+[cstring])
                else :
                    continue

    def isRecu(self,s):
        rs=s[::-1]
        return rs==s
    def partition(self, s):
        self.res=[]
        self.dfs(s,[])
        return self.res
