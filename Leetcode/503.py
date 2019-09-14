# https://leetcode.com/problems/next-greater-element-ii/submissions/
# T: O(n)
# S: O(n)

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [-1]*length
        stack = []
        
        for i in range(length*2):
            num = nums[i % length]
            while stack and nums[stack[-1]] < num:
                result[stack.pop()] = num
                
            if i < length:
                stack.append(i)
                
        return result
        