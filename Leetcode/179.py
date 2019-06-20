# https://leetcode.com/problems/largest-number/
# Use Python's cmp method to compare "5", "9". "59" < "95".
# https://docs.python.org/3/howto/sorting.html
# 面试极少出现
# T: O(nlogn)
# S: O(n)

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums or len(nums) == 0:
            return ''
        
        nums = [str(x) for x in nums]
        nums.sort(key = cmp_to_key(lambda x, y: int(y + x) - int(x + y)))
        return ''.join(nums).lstrip('0') or '0'
        
        
            