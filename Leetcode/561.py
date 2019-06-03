# https://leetcode.com/problems/array-partition-i/
# T: O(nlogn)
# T: O(1)

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        
        for i in range(0, len(nums), 2):
            result += nums[i]
            
        return result