# -*- coding: UTF-8 -*-
class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """

    def isMatch(self, s, p):
        # write your code here
        m=len(s)
        n=len(p)
        s_index,p_index,s_last,p_last=0,0,-1,-1
        while s_index<m:
            if p_index<n and p[p_index] in (s[s_index],'.'):
                p_index+=1
                s_index+=1
            elif p_index+1<n and p[p_index+1]=='*':
                p_index+=2
                p_last=p_index
            elif p[p_index]=='*':
                s_index+=1
                s_last=s_index
                p_index=p_last
            elif p_last !=-1:
                p_index+=1
                s_index=s_last
            else :
                return  False
        while p_index+1<n and p[p_index+1]=='*':
            p_index+=2
        return p_index==n



print Solution().isMatch("aab","c*a*b") == True
print Solution().isMatch("aasdfasdfasdfasdfas","aasdf.*asdf.*asdf.*asdf.*s") == True
print Solution().isMatch("acaabbaccbbacaabbbb","a*.*b*.*a*aa*a*") == False
print Solution().isMatch("aa",".*")
print Solution().isMatch("aa","aa")
print Solution().isMatch("bbbba",".*a*a")
print Solution().isMatch("aab","c*a*b")
print Solution().isMatch("acaabbaccbbacaabbbb","a*.*b*.*a*aa*a*")
