class Solution:
    def searchInsert(self, A, target):
        # write your code here
        if not A:
            return 0
        start,end=0,len(A)
        while start+1<end:
            mid=(start+end)/2
            if A[mid]<target:
                start=mid
            else :
                end=mid
        if target<=A[start]:
            return start
        return end
print Solution().searchInsert([1,2,3,4,5,9],0)