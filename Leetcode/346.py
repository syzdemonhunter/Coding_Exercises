# https://leetcode.com/problems/moving-average-from-data-stream/
# T: O(n)
# S: O(n)

import collections
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.q = collections.deque([])
        self.total = 0
        
    def next(self, val: int) -> float:
        if len(self.q) == self.size:
            self.total -= self.q.popleft()
            
        self.total += val
        self.q.append(val)
        return self.total/len(self.q)
            

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)