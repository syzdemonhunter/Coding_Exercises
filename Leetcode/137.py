# https://leetcode.com/problems/single-number-ii/
# 这道题不重要
# T: O(n)
# S: O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        
        for num in nums:
            ones = (ones^num) & ~twos
            twos = (twos^num) & ~ones
            
        return ones