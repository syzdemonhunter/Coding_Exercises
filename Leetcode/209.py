# https://leetcode.com/problems/minimum-size-subarray-sum/
# T: O(n)
# S: O(1)

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        result = sys.maxsize 
        left, total = 0, 0
        
        for i in range(len(nums)):
            total += nums[i]
            while left <= i and total >= s:
                result = min(result, i - left + 1)
                total -= nums[left]
                left += 1
            
        return 0 if result == sys.maxsize else result