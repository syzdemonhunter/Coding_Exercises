# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# T: O(logn)
# S: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) == 0:
            return [-1, -1]
        start = self.find_first(nums, target)
        if start == -1:
            return [-1, -1]
        end = self.find_last(nums, target)
        return [start, end]
        
        
    def find_first(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start)//2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
                
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
        
    def find_last(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start)//2
            if nums[mid] > target:
                end = mid
            else:
                start = mid
                
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1