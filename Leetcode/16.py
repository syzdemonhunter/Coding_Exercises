# https://leetcode.com/problems/3sum-closest/
# T: O(nlogn)
# S: O(1)

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 3:
            return -1
        
        nums.sort()
        result = None
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if result is None or abs(total - target) < abs(result - target):
                    result = total
                    
                if total <= target:
                    left += 1
                else:
                    right -= 1
                    
        return result