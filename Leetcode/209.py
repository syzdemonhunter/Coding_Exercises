# https://leetcode.com/problems/minimum-size-subarray-sum/
# https://medium.com/@lenchen/leetcode-209-minimum-size-subarray-sum-ab92c2de4e94
# T: O(n)
# S: O(1)

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i, total, min_count = 0, 0, len(nums) + 1
        
        for j in range(len(nums)):
            total += nums[j]
            
            while total >= s:
                new_count = j - i + 1
                if new_count < min_count:
                    min_count = new_count
                    
                total -= nums[i]
                i += 1
                
        if min_count > len(nums):
            return 0
        else:
            return min_count