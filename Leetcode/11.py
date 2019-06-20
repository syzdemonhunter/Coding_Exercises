# https://leetcode.com/problems/container-with-most-water/
# T: O(n)
# S: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        l, r = 0, len(height) - 1
        while l < r:
            result = max(result, min(height[l], height[r])*(r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return result
        