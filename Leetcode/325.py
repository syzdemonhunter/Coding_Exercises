# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
# T: O(n)
# S: O(n)

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        result = 0
        dic = {}
        dic[0] = -1
        
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            
        for i in range(len(nums)):
            if nums[i] - k in dic:
                result = max(result, i - dic[nums[i] - k])
                
            if nums[i] not in dic:
                dic[nums[i]] = i
                
        return result
        
        