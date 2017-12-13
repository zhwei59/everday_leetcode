class Solution:
    """
    @param: A: an integer sorted array
    @param: target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        # write your code here
        if not A:
            return [-1, -1]
        n = len(A)
        left, right = 0, n - 1
        while left + 1 < right:
            mid = (left + right) / 2
            if A[mid] < target:
                left = mid
            else:
                right = mid

        start=-1
        if A[left]==target:
            start=left
        if A[right]==target and start==-1:
            start=right

        left, right = start , n - 1
        while left + 1 < right:
            mid = (left + right) / 2
            if A[mid] <= target:
                left = mid
            else:
                right = mid
        end = -1

        if A[right] == target :
            end = right
        if A[left] == target and end == -1:
            end = left

        return [start, end]
print Solution().searchRange([5, 7, 7, 8, 8, 10],8)