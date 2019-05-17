# https://leetcode.com/problems/kth-largest-element-in-a-stream/
# T: O(n*log(k))
# S: O(k)

import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.length = k
        self.data = []
        for num in nums:
            self.add(num)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.data) < self.length:
            heapq.heappush(self.data, val)
        else:
            min_val = self.data[0]
            if val > min_val:
                heapq.heappop(self.data)
                heapq.heappush(self.data, val)
        return self.data[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)