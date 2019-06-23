# https://leetcode.com/problems/maximum-gap/
# bucket sort
# 几乎不考
# T: O(n)
# S: O(n)

import math
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return 0
        
        num_len = len(nums)
        max_val, min_val = nums[0], nums[0]
        
        for i in range(num_len):
            max_val = max(max_val, nums[i])
            min_val = min(min_val, nums[i])
        
        gap = math.ceil((max_val - min_val)/ (num_len - 1))
        bucket_min = [float('inf')]*(num_len - 1)
        bucket_max = [-float('inf')]*(num_len - 1)
        
        for num in nums:
            if num == min_val or num == max_val:
                continue
            bucket = (num - min_val)//gap
            bucket_min[bucket] = min(num, bucket_min[bucket])
            bucket_max[bucket] = max(num, bucket_max[bucket])
            
        result = 0
        pre = min_val
        for i in range(num_len - 1):
            if bucket_min[i] == float('inf') and bucket_max[i] == -float('inf'):
                continue
            result = max(result, bucket_min[i] - pre)
            pre = bucket_max[i]
            
        result = max(result, max_val - pre)
        return result
        
        