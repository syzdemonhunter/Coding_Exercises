# https://leetcode.com/problems/merge-intervals/
# T: O(nlogn)
# S: O(n)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) <= 1:
            return intervals
        
        intervals = sorted(intervals)
        start, end = intervals[0][0], intervals[0][1]
        result = []
        
        for interval in intervals:
            if interval[0] <= end:
                end = max(end, interval[1])
            else:
                result.append([start, end])
                start = interval[0]
                end = interval[1]
                
        result.append([start, end])
        return result