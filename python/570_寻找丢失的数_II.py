class Solution:
    """
    @param: n: An integer
    @param: str: a string with number from 1-n in random order and miss one number
    @return: An integer
    取一个
    """
    def dfs(self,n,sub,curr):
        if len(sub)==0 :
            if len(curr)==n-1:
                print curr
                test=[i for i in range(n+1)]
                for c in range(1,n+1):
                    if c in curr:
                        test[c]=0
                self.res=max(self.res,max(test))
        else :
            for i in range(2):
                scurr=sub[:i+1]
                if(scurr[0] !='0') :
                    cs=int(scurr)
                    if cs<=n:
                        if cs not in curr:
                            self.dfs(n,sub[i+1:],curr+[cs])
    def findMissing2(self, n, stri):
        # write your code here
        self.res=0
        self.dfs(n,stri,[])
        return self.res