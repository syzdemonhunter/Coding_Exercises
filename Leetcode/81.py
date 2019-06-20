# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# T: O(logn) (worst: O(n))
# S: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums or len(nums) == 0:
            return False
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = end + (start - end)//2
            if nums[mid] == target:
                return True
            if nums[start] == nums[mid] and nums[mid] == nums[end]:
                start += 1
                end -= 1
                
            elif nums[start] <= nums[mid]:
                if nums[start] <= target and target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target and target <= nums[end]:
                    start = mid
                else:
                    end = mid
                    
        if nums[start] == target:
            return True
        if nums[end] == target:
            return True
        
        return False
        