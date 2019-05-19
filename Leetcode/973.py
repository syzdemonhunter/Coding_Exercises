# https://leetcode.com/problems/k-closest-points-to-origin/
# T: O(nlogk)
# S: O(k)

import math, heapq

class Solution(object):
    
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        max_heap = []
        for i in range(len(points)):
            p_i = points[i]
            heapq.heappush(max_heap, (-(p_i[0]**2 + p_i[1]**2), p_i))
            
            if len(max_heap) == K + 1:
                heapq.heappop(max_heap)
                
        return [s[1] for s in heapq.nlargest(K, max_heap)]