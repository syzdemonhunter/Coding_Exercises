# https://leetcode.com/problems/moving-average-from-data-stream/
# 使用队列保存窗口中的数，然后计算和。

import collections

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()
        self.size = size
        self.total = 0

    def next(self, val: int) -> float:
        if len(self.q) == self.size:
            self.total -= self.q.popleft()
            
        self.total += val
        self.q.append(val)
        return self.total / len(self.q)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)