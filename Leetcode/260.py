# https://leetcode.com/problems/single-number-iii/
# T: O(n)
# S: O(1)


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        xor, mask = 0, 1
        for num in nums:
            xor ^= num
        while xor & mask == 0:
            mask = mask << 1
        x, y = 0, 0
        for num in nums:
            if num & mask == 0:
                x ^= num
            else:
                y ^= num
        return [x, y]