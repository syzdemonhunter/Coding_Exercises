# https://leetcode.com/problems/maximal-rectangle/

'''
# T: O(m*n)
# S: O(n)
# DP
# left[]: 从左到右，出现连续'1'的string的第一个坐标
# right[]: 从右到做，出现连续'1'的string的最后一个坐标
# height[]: 从上到下的高度
# result: (right[j] - left[j])*height[j]
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if not matrix or m == 0:
            return 0
        
        n = len(matrix[0])
        result = 0
        height = [0]*n
        left = [0]*n
        right = [n]*n
        
        for i in range(m):
            cur_left = 0
            cur_right = n
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
                    
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(cur_left, left[j])
                else:
                    left[j] = 0
                    cur_left = j + 1
                    
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(cur_right, right[j])
                else:
                    right[j] = n
                    cur_right = j
                    
            for j in range(n):
                result = max(result, (right[j] - left[j])*height[j])
                
        return result
'''
# T: O(m*n)
# S: O(n)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix[0])
        height = [0]*(n + 1)
        ans = 0
        
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h*w)
                stack.append(i)
                
        return ans


        
        