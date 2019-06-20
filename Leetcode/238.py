# https://cspiration.com/course/video?id=1185
# T: O(n)
# S: O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 0:
            return nums
        
        result = [0]*len(nums)
        result[0] = 1
        for i in range(1, len(nums)):
            result[i] = result[i - 1]*nums[i - 1]
            
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= right
            right *= nums[i]
            
        return result
        