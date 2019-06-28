# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

'''
# T: O(nlogn)
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
'''
# T: O(n*log(max_val - min_val))
# S: O(1)

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left = matrix[0][0]
        right = matrix[n - 1][n - 1]
        while left + 1 < right:
            mid = left + (right - left)//2
            num = self.count(matrix, mid)
            if num >= k:
                right = mid
            else:
                left = mid
                
        if self.count(matrix, right) <= k - 1:
            return right
        return left
    
    def count(self, matrix, target):
        n = len(matrix)
        result = 0
        i = n - 1
        j = 0
        
        while i >= 0 and j < n:
            if matrix[i][j] < target:
                result += i + 1
                j += 1
            else:
                i -= 1
            
        return result