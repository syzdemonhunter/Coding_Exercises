# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
# T: O(n) (worst), usually O(logn)
# S: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return -1
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start)//2
            if nums[mid] < nums[end]:
                end = mid
            elif nums[mid] > nums[end]:
                start = mid + 1
            else:
                end -= 1
                
        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]
                
        