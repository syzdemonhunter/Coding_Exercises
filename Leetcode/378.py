# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# T: O(klogk)
# S: O(n)

import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = [(matrix[0][y], 0, y) for y in range(len(matrix[0]))]
        heapq.heapify(min_heap)
        
        res = 0
        for i in range(k):
            res, x, y = heapq.heappop(min_heap)
            if x + 1 < len(matrix):
                heapq.heappush(min_heap, (matrix[x + 1][y], x + 1, y))
        return res
            