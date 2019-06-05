# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
# T: O(n)
# S: O(1)

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        sum_num = sum(nums)
        min_num = min(nums)
        
        return sum_num - min_num*len(nums)
        