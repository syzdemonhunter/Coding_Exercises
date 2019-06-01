# https://leetcode.com/problems/k-diff-pairs-in-an-array/
# T: O(n)
# S: O(1)

import collections
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        result = 0
        count = collections.Counter(nums)
        for num in count:
            if k > 0 and num + k in count or k == 0 and count[num] > 1:
                result += 1
                
        return result
                