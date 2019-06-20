# https://leetcode.com/problems/maximum-product-subarray/
# T: O(n)
# S: O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        max_val = nums[0]
        min_val = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):
            tmp = max_val
            max_val = max(max(max_val*nums[i], min_val*nums[i]), nums[i])
            min_val = min(min(tmp*nums[i], min_val*nums[i]), nums[i])
            result = max(result, max_val)
        return result
        