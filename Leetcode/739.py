# https://leetcode.com/problems/daily-temperatures/
# 利用stack记录温度对应的index，如果当前温度值大于栈顶index对应的温度值，就pop
# T: O(n)
# S: O(n)

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T or len(T) == 0:
            return []
        
        result = [0]*len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return result
        