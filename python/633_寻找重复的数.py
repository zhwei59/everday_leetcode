class Solution:
    """
    @param: nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one

    0,1,2,3,4,5
    [5,5,4,3,2,1] 6/2=3
    [5,4,3,2,1]
    """

    def findDuplicate(self, nums):
        # write your code here
        nums.sort()
        m = len(nums)
        left, right = 0, m - 1
        while left+1<right:
            mid=(left+right)/2
            dc=nums[mid]
            if nums[mid]==nums[mid-1]:
                left=mid
                break
            if nums[mid]== mid+1:
                left=mid
            else:
                right=mid
        return nums[left]
print Solution().findDuplicate([85,42,42,42,51,17,42,42,40,99,75,42,42,12,87,42,92,30,42,42,42,42,39,86,42,22,49,53,42,42,42,42,33,1,21,65,70,9,88,46,42,42,81,15,68,42,26,67,34,31,82,42,5,42,50,66,58,42,42,57,42,42,42,16,42,42,42,42,20,23,42,42,79,89,45,28,42,42,7,42,13,83,74,42,42,69,43,27,71,10,42,72,42,42,78,98,11,25,42,2])