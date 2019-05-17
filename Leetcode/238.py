# https://leetcode.com/problems/product-of-array-except-self/
# T: O(n)
# S: O(1)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        right = 1
        length = len(nums)
        
        result = []
        result.append(1)
        for i in range(1, length):
            result.append(result[i-1]*nums[i-1])
            
        for i in range(length - 1, -1, -1):
            result[i] *= right
            right *= nums[i]
            
        return result
        