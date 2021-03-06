# https://leetcode.com/problems/find-median-from-data-stream/
# T: O(logn)
# S: O(n)

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        
    def rebalance(self):
        while len(self.min_heap) < len(self.max_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            
        while len(self.min_heap) > len(self.max_heap) + 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == 0:
            heapq.heappush(self.min_heap, -num)
            return
        
        left = -self.min_heap[0]
        if num <= left:
            heapq.heappush(self.min_heap, -num)
            
        else:
            heapq.heappush(self.max_heap, num)
            
        self.rebalance()
        

    def findMedian(self) -> float:
        left = -self.min_heap[0]
        if len(self.min_heap) == len(self.max_heap):
            right = self.max_heap[0]
            return (left + right) / 2.0
        return left*1.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()