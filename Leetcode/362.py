# https://leetcode.com/problems/design-hit-counter/

import collections
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()
        self.count = 0

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.q.append(timestamp)
        self.count += 1
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        start = timestamp - 300
        i = 0
        while i < self.count and self.q[i] <= start:
            self.q.popleft()
            self.count -= 1
        return self.count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)