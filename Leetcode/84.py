# https://leetcode.com/problems/largest-rectangle-in-histogram/
# 考的次数不多，是个典型的stack题目
# T: O(n)
# S: O(n)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights or len(heights) == 0:
            return 0
        
        result = 0
        stack = []
        
        for i in range(len(heights) + 1):
            h = 0 if i == len(heights) else heights[i]
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                start = -1 if not stack else stack[-1]
                area = height*(i - start - 1)
                result = max(result, area)
            stack.append(i)
    
        return result