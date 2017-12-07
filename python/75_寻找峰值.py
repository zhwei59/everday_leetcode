class Solution:
    def findPeak(self, A):
        left,right=1,len(A)-1
        while left+1<right:
            mid=(left+right)/2
            if A[mid]<A[mid-1]:
                right=mid
            elif A[mid]<A[mid+1]:
                left=mid
            else:
                right=mid
        if A[left]<A[right]:
            return right
        return left


