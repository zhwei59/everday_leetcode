# -*- coding: UTF-8 -*-
class Solution:
    """
    @param: s: A string
    @param: p: A string includes "?" and "*"
    @return: is Match?
    """
## dfs 无脑暴力搜索
    def dfs(self, s, p):
        if not s and not p:
            return True
        if not s :
            return p.count('*')==len(p)
        if not p:
            return False
        if p[-1] != '*':
            if s[-1] == p[-1] or p[-1] == '?':
                return self.dfs(s[:-1], p[:-1])
            return False
        else:
            return self.dfs(s, p[:-1]) or self.dfs(s[:- 1], p)
## 通过 p 和s 交替上升 s[i] 碰到p[j]是一定要跳出的
    def isMatch(self, s, p):
        # write your code hero
        if not s and not p:
            return True
        if not s :
            return p.count('*')==len(p)
        if not p:
            return False
        s_index,p_index,s_last,p_last=0,0,-1,-1
        while s_index<len(s) :
            if p_index<len(p) and p[p_index] in (s[s_index],'?'):
                s_index+=1
                p_index+=1
            elif  p_index<len(p) and  p[p_index]=='*':
                p_index+=1
                s_last=s_index
                p_last=p_index
            elif p_last !=-1:
                s_last+=1
                s_index=s_last
                p_index=p_last
            else :
                return  False
        while p_index<len(p) and p_index=='*':
            p_index+=1
        return p_index==len(p)










print Solution().isMatch("abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb","**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb")
print Solution().isMatch("abqbc","a*qbq*")
print Solution().isMatch("aa","a*")
print Solution().isMatch("aa","a")
