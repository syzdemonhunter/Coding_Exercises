# https://leetcode.com/problems/3sum-smaller/
# T: O(n^2)
# S: O(1)

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        result = 0
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < target:
                    result += right - left
                    left += 1
                else:
                    right -= 1
                    
        return result
        
        