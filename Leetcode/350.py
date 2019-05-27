# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# 用dict维护前一个数组中每个值出现的次数
# 然后遍历第二个数组，对于每个遍历到的数，在dict中将这个数出现的次数-1
# T: O(n)
# S: O(n)

import collections

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = collections.Counter(nums1)
        result = []
        
        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1
                
        return result
        