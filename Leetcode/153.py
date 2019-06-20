# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# T: O(logn)
# S: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = end + (start - end)//2
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid + 1
                
        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]