# https://www.youtube.com/watch?v=FrWq2rznPLQ
# https://leetcode.com/problems/kth-largest-element-in-an-array/

# T: O(n*log(k))
# S: O(k)

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num) 
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return heapq.heappop(min_heap)
        