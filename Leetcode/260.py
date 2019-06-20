# https://leetcode.com/problems/single-number-iii/
# 位运算，不用多看。面试中不怎么考
# T: O(n)
# S: O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = 0
        for num in nums:
            diff ^= num
        diff &= -diff
        result = [0, 0]
        for num in nums:
            if num & diff == 0:
                result[0] ^= num
            else:
                result[1] ^= num
        return result
                