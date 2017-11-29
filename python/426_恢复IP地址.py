class Solution:
    """
    @param: s: the IP string
    @return: All possible valid IP addresses
    """
    def dfs(self,s,curr):
        if len(curr)==4 and not s:
            self.res.append('.'.join(curr))
            return
        else:
            if not s :
                return
            else:
                for i in range(0,3):
                    if s[0]=='0' and i>0:
                        return
                    ip=s[0:i+1]
                    if int(ip)<256:
                        c=curr+[ip]
                        self.dfs(s[i+1:],c)
                return
    def restoreIpAddresses(self, s):
        # write your code here
        # 输入
        self.res=[]
        self.dfs(s,[])

        return sorted(self.res)
