# https://leetcode.com/problems/sort-characters-by-frequency/
# T: O(n)
# S: O(n)

import heapq, collections

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_heap = []
        d = collections.Counter(s)
        
        for k, v in d.items():
            heapq.heappush(max_heap, (-v, k))
            
        res = ''
        while max_heap:
            v, k = heapq.heappop(max_heap)
            res += k*abs(v)
            
        return res
        