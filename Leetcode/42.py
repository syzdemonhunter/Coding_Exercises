# https://leetcode.com/problems/trapping-rain-water/
# https://www.youtube.com/watch?v=2LjNzbK2cmA
# time: O(n)
# space: O(1)

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        res = 0
        left_max, right_max = 0, 0
        
        while left < right:
            if height[left] < height[right]:
                left_max = max(height[left], left_max)
                res += left_max - height[left]
                left += 1
                
            else:
                right_max = max(height[right], right_max)
                res += right_max - height[right]
                right -= 1
                
        return res