# https://leetcode.com/problems/container-with-most-water/
# T: O(n)
# S: O(1)


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        i, j = 0, len(height) - 1
        max_vol = 0
        while i <= j:
            vol = (j - i)*min(height[j], height[i])
            max_vol = max(max_vol, vol)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
                
        return max_vol