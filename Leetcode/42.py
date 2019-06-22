# https://leetcode.com/problems/trapping-rain-water/
# T: O(n)
# S: O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0
        left_max, right_max = 0, 0
        
        while left < right:
            if height[left] < height[right]:
                left_max = max(height[left], left_max)
                result += left_max - height[left]
                left += 1
            else:
                right_max = max(height[right], right_max)
                result += right_max - height[right]
                right -= 1
                
        return result
                