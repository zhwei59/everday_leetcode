class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        m=len(A)
        n=len(B)
        res=0
        for i in range(m):
            for j in range(n):
                curr=0
                while i+curr<m and j+curr<n and A[i+curr]==B[j+curr]:
                    curr+=1
                res=max(res,curr)
        return res