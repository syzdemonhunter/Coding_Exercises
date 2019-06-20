# https://leetcode.com/problems/missing-number/
'''
# T: O(n)
# S: O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i in range(len(nums)):
            result ^= i ^ nums[i]
        return result
'''
# T: O(n)
# S: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_exp = len(nums)*(len(nums) + 1)/2
        total_actual = 0
        for num in nums:
            total_actual += num
            
        return int(total_exp - total_actual)
        