# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times = collections.defaultdict(list)
        self.values = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)
        
    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect(self.times[key], timestamp)
        return self.values[key][idx - 1] if idx else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)